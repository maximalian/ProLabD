import pulp
from db import database_connection
from utils import to_float


def calculate_diet(age, height, weight, gender=1, selected_products=[], user_max_limits={}, user_min_limits={}, store="both"):
    """
    Aprēķina optimālu uztura plānu, ņemot vērā lietotāja parametrus un pieejamos produktus.

    Parametri:
    - age: Lietotāja vecums gados.
    - height: Lietotāja augums centimetros.
    - weight: Lietotāja svars kilogramos.
    - gender: Lietotāja dzimums (1 = vīrietis, 0 = sieviete).
    - selected_products: Produkti, kurus lietotājs izvēlējies.
    - user_max_limits: Maksimālie ierobežojumi produktiem.
    - user_min_limits: Minimālie ierobežojumi produktiem.
    - store: Veikala izvēle (Maxima, Rimi vai abi).

    Atgriež:
    - Optimizēts uztura plāns vai kļūdu ziņojums.
    """

    try:
        # Izveido savienojumu ar datubāzi un iegūst visus pieejamos produktus
        with database_connection() as cursor:
            cursor.execute("SELECT * FROM produkts;")
            records = cursor.fetchall()
    except Exception as db_error:
        # Ja rodas kļūda, atgriež kļūdas ziņojumu
        return {"Error": f"Database error: {db_error}"}

    # Pārbauda, vai datubāzē ir pieejami produkti
    if not records:
        return {"Error": "No products found in the database."}

    # Iniciē tukšus sarakstus datu glabāšanai
    ind, name, kal, olb, tau, ogl, cen, maxima_price, rimi_price, maxima_link, rimi_link, mer = ([] for _ in range(12))

    # Apstrādā katru produktu un filtrē pēc lietotāja parametriem
    for row in records:

        # Pārbauda, vai produkts atbilst ierobežojumiem vai ir izvēlēts
        if str(row[0]) in user_min_limits or str(row[0]) in user_max_limits:
            pass  # Produktu vienmēr iekļauj
        elif row[0] in selected_products:
            continue

        # Iegūst produkta cenu no Maxima un Rimi
        cenM = to_float(row[6])  # Cena Maxima
        cenR = to_float(row[7])  # Cena Rimi

        # Izvēlas cenu atkarībā no veikala
        if store == "Maxima" and cenM > 0:
            price = cenM
        elif store == "Rimi" and cenR > 0:
            price = cenR
        elif store == "both":
            # Ja tiek izvēlēti abi veikali, izvēlas minimālo cenu
            price = min(filter(lambda x: x > 0, [cenM, cenR]), default=None)
        else:
            continue

        # Ja cena nav atrasta, produkts tiek izlaists
        if price is None:
            continue

        # Saglabā produkta datus attiecīgajos sarakstos
        ind.append(row[0])
        name.append(row[1])
        kal.append(to_float(row[2]) or 0)
        olb.append(to_float(row[3]) or 0)
        tau.append(to_float(row[4]) or 0)
        ogl.append(to_float(row[5]) or 0)
        maxima_link.append(row[8])  # saite_maxima
        rimi_link.append(row[9])    # saite_rimi
        cen.append(price)
        maxima_price.append(cenM)
        rimi_price.append(cenR)
        mer.append(row[10] if row[10] else "kg")

    # Ja neviens produkts neatbilst kritērijiem, atgriež kļūdu
    if not ind:
        return {"Error": "No suitable products found for the selected criteria."}

    # Aprēķina uzturvērtības normas, pamatojoties uz lietotāja parametriem https://www.calculator.net/protein-calculator.html
    norm_kcal = (13.397 * weight + 4.799 * height - 5.677 * age + 88.362) if gender else (
        9.247 * weight + 3.098 * height - 4.330 * age + 447.593)
    norm_protein = 1.3 * weight
    norm_fat = (norm_kcal * 0.3) / 9
    norm_carbs = (norm_kcal * 0.5) / 4


    lower_tolerance = 0.90
    upper_tolerance = 1.20

    # Izveido optimizācijas problēmu izmaksu minimizācijai
    problem = pulp.LpProblem("Minimum_Cost_Diet", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x_{i}", lowBound=0, cat="Continuous") for i in range(len(ind))]

    # Pievieno optimizācijas ierobežojumus
    problem += pulp.lpSum(cen[i] * x[i] for i in range(len(ind))), "Total Cost"
    problem += pulp.lpSum(olb[i] * x[i] for i in range(len(ind))) >= norm_protein * lower_tolerance, "Protein_Lower_Limit"
    problem += pulp.lpSum(olb[i] * x[i] for i in range(len(ind))) <= norm_protein * upper_tolerance, "Protein_Upper_Limit"
    problem += pulp.lpSum(tau[i] * x[i] for i in range(len(ind))) >= norm_fat * lower_tolerance, "Fat_Lower_Limit"
    problem += pulp.lpSum(tau[i] * x[i] for i in range(len(ind))) <= norm_fat * upper_tolerance, "Fat_Upper_Limit"
    problem += pulp.lpSum(ogl[i] * x[i] for i in range(len(ind))) >= norm_carbs * lower_tolerance, "Carbs_Lower_Limit"
    problem += pulp.lpSum(ogl[i] * x[i] for i in range(len(ind))) <= norm_carbs * upper_tolerance, "Carbs_Upper_Limit"
    problem += pulp.lpSum(kal[i] * x[i] for i in range(len(ind))) >= norm_kcal * lower_tolerance, "Calories_Lower_Limit"
    problem += pulp.lpSum(kal[i] * x[i] for i in range(len(ind))) <= norm_kcal * upper_tolerance, "Calories_Upper_Limit"

    # Pievieno lietotāja definētos minimālos un maksimālos ierobežojumus
    for i in range(len(ind)):
        if str(ind[i]) in user_max_limits and user_max_limits[str(ind[i])] is not None:
            problem += x[i] <= user_max_limits[str(ind[i])], f"Max_Limit_{ind[i]}"
        if str(ind[i]) in user_min_limits and user_min_limits[str(ind[i])] is not None:
            problem += x[i] >= user_min_limits[str(ind[i])], f"Min_Limit_{ind[i]}"

    # Atrisina optimizācijas problēmu
    problem.solve()

    # Pārbauda, vai risinājums ir optimāls
    if pulp.LpStatus[problem.status] != "Optimal":
        return {"Error": "No optimal solution found."}

    # Sagatavo rezultātu atgriešanai
    results = {
        "Cena": round(pulp.value(problem.objective), 2),
        "Edienkarte": [
            {
                "name": name[i],
                "quantity": round(x[i].varValue, 2),
                "unit": mer[i],
                "price": cen[i],
                "maxima_price": maxima_price[i],
                "rimi_price": rimi_price[i],
                "maxima_link": maxima_link[i],
                "rimi_link": rimi_link[i],
                "protein": round(olb[i] * x[i].varValue, 2),
                "fat": round(tau[i] * x[i].varValue, 2),
                "carbs": round(ogl[i] * x[i].varValue, 2),
                "calories": round(kal[i] * x[i].varValue, 2),
            }
            for i in range(len(ind)) if x[i].varValue > 0
        ],
        "norms": {
            "Protein": round(norm_protein, 2),
            "Fat": round(norm_fat, 2),
            "Carbs": round(norm_carbs, 2),
            "Calories": round(norm_kcal, 2),
        }
    }

    # Aprēķina uzturvērtību kopējos rādītājus
    total_proteins = sum(item["protein"] for item in results["Edienkarte"])
    total_fats = sum(item["fat"] for item in results["Edienkarte"])
    total_carbs = sum(item["carbs"] for item in results["Edienkarte"])
    total_calories = sum(item["calories"] for item in results["Edienkarte"])

    # Pievieno uzturvērtību kopsavilkumu
    results["nutrients"] = {
        "Proteins": round(total_proteins, 2),
        "Fats": round(total_fats, 2),
        "Carbohydrates": round(total_carbs, 2),
        "Calories": round(total_calories, 2),
    }

    return results
