def calculate_diet(age, height, weight, gender=1):
    """
    Calculate daily caloric needs based on user inputs.

    :param age: Age of the user in years
    :param height: Height of the user in centimeters
    :param weight: Weight of the user in kilograms
    :param gender: Gender of the user ('male'=1 or 'female'=0)
    :return: A dictionary containing the calculated daily caloric needs and macronutrient distribution.
    """

    # Import necessary libraries
    import psycopg2
    import pulp
    from decimal import Decimal

    # Database configuration parameters
    db_config = {
        'dbname': 'prolab24',
        'user': 'root',
        'password': 'prolab24',
        'host': '13.61.89.142',
        'port': '5432'
    }

    try:
        # Establish connection to the PostgreSQL database
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        query = "SELECT * FROM produkts;"
        cursor.execute(query)
        records = cursor.fetchall()  # Fetch all records from the database
    except (Exception, psycopg2.Error) as error:
        return None
    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

    # Safety check to avoid None values during comparisons
    def safe_min(num):
        if num is None:
            return Decimal('9999')  # Use a large value to avoid interference with minimum calculations
        return Decimal(num)

    # Combine two arrays with minimal values from each index
    def safe_array(arr1, arr2):
        minarr = []
        for i in range(len(arr1)):
            minarr.append(min(safe_min(arr1[i]), safe_min(arr2[i])))
        return minarr

    if not records:
        return None

    # Separate records into individual lists
    ind = [row[0] for row in records]
    name = [row[1] for row in records]
    kal = [row[2] for row in records]
    olb = [row[3] for row in records]
    tau = [row[4] for row in records]
    ogl = [row[5] for row in records]
    cenM = [row[6] for row in records]
    cenR = [row[7] for row in records]
    saiM = [row[8] for row in records]
    saiR = [row[9] for row in records]
    mer = [row[10] for row in records]
    cen = safe_array(cenM, cenR)

    # Formulas for calculating daily norms https://www.calculator.net/protein-calculator.html
    if gender:
        norm_kca = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        norm_kca = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    norm_olb = 1.7 * weight
    norm_tau = 0.9 * weight
    norm_ogl = (norm_kca - norm_olb * 4 - norm_tau * 9) / 4

    # Linear programming algorithm for minimum cost diet
    problem = pulp.LpProblem("Minimum_Cost_Diet", pulp.LpMinimize)

    # Define variables
    x = [pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(len(records))]

    # Objective function: Minimize cost
    problem += pulp.lpSum(float(cen[i]) * x[i] / 10 for i in range(len(records)))

    # Constraints to meet nutritional requirements
    problem += pulp.lpSum(float(olb[i]) * x[i] / 10 for i in range(len(records))) >= norm_olb
    problem += pulp.lpSum(float(tau[i]) * x[i] / 10 for i in range(len(records))) >= norm_tau
    problem += pulp.lpSum(float(ogl[i]) * x[i] / 10 for i in range(len(records))) >= norm_ogl
    problem += pulp.lpSum(float(kal[i]) * x[i] / 10 for i in range(len(records))) >= norm_kca

    problem.solve()

    # Summation variables
    solb, stau, sogl, skca = 0, 0, 0, 0
    # Dictionary to store results
    results = {}
    if pulp.LpStatus[problem.status] == "Optimal":
        results["Cena"] = str(round(pulp.value(problem.objective), 2)) + " eiro"
        results["Edienkarte"] = []
        for i, var in enumerate(x):
            if var.varValue:
                solb += float(olb[i]) * var.varValue / 10
                stau += float(tau[i]) * var.varValue / 10
                sogl += float(ogl[i]) * var.varValue / 10
                skca += float(kal[i]) * var.varValue / 10

                # Determine the price and website based on availability
                if cenM[i] is not None and cenR[i] is not None:
                    if safe_min(cenM[i]) > safe_min(cenR[i]):
                        cena = cenR[i]
                        site = saiR[i]
                    else:
                        cena = cenM[i]
                        site = saiM[i]
                elif cenM[i] is not None:  # Only cenM exists
                    cena = cenM[i]
                    site = saiM[i]
                elif cenR[i] is not None:  # Only cenR exists
                    cena = cenR[i]
                    site = saiR[i]
                else:
                    # Skip this entry if both cenM and cenR are None
                    continue

                results["Edienkarte"].append(
                    f"{name[i]} : {var.varValue / 10} {mer[i]} Cena: {cena} tīmekļa vietne: {site}"
                )
        results["solb"] = round(solb, 2)
        results["stau"] = round(stau, 2)
        results["sogl"] = round(sogl, 2)
        results["skca"] = round(skca, 2)
        results["nolb"] = round(norm_olb, 2)
        results["ntau"] = round(norm_tau, 2)
        results["nogl"] = round(norm_ogl, 2)
        results["nkca"] = round(norm_kca, 2)
    else:
        results["Error"] = "No optimal solution found."
    return results
