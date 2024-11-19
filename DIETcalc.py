def calculate_diet(age, height, weight, gender = 1, vegan = 0, productsType = 0, categories = []):
	"""
	    Calculate daily caloric needs based on user inputs.

	    :param age: Age of the user in years
	    :param height: Height of the user in centimeters
	    :param weight: Weight of the user in kilograms
	    :param gender: Gender of the user ('male'=1 or 'female'=0)
	    :param vegan: Dietary preference. ('vegan'=1 or 'non-vegan'=0)
	    :param productsType: Product type selector (0 for normal, 1 for selected categories).
	    :param categories: List of boolean values indicating selected categories if productsType is 1.
	    :return: A dictionary containing the calculated daily caloric needs and macronutrient distribution.
	"""

	# Import necessary libraries
	import psycopg2
	import pulp
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
			return 9999
		return num

	# Combine two arrays with minimal values from each index
	def safe_array(arr1, arr2):
		minarr = []
		for i in range(len(arr1)):
			minarr.append(min(safe_min(arr1[i]), safe_min(arr2[i])))
		return minarr

	if records:
		pass
	else:
		return None

	# Separate records into individual lists
	ind = []
	name = []
	kal = []
	olb = []
	tau = []
	ogl = []
	cenM = []
	cenR = []
	saiM = []
	saiR = []
	mer = []
	kat = []
	katK = []
	veg = []
	cen = []
	for row in records:
		if int(vegan) == 1:
			if int(row[13]) == 0:
				continue
		if productsType == 1:
			if categories[int(row[12]) - 1] == 0:
				continue
		ind.append(row[0])
		name.append(row[1])
		kal.append(row[2])
		olb.append(row[3])
		tau.append(row[4])
		ogl.append(row[5])
		cenM.append(row[6])
		cenR.append(row[7])
		saiM.append(row[8])
		saiR.append(row[9])
		mer.append(row[10])
		kat.append(row[11])
		katK.append(row[12])
		veg.append(row[13])
	cen = safe_array(cenM, cenR)

	# Formulas for calculating daily norms
	if (gender):
		norm_kca = (13.397 * weight) + (4.799 * height) - (5.677 * age) + 88.362  # Revised Harris-Benedict Equation
	else:
		norm_kca = (9.247 * weight) + (3.098 * height) - (4.330 * age) + 447.593  # Revised Harris-Benedict Equation

	norm_olb = 1.3 * weight  # https://www.calculator.net/protein-calculator.html  0.8-1.8 depending on factors
	norm_tau = (norm_kca * 0.3) / 4  # https://www.calculator.net/fat-intake-calculator.html
	norm_ogl = (norm_kca * 0.5) / 4  # https://www.calculator.net/carbohydrate-calculator.html

	# Linear programming algorithm for minimum cost diet
	problem = pulp.LpProblem("Minimum_Cost_Diet", pulp.LpMinimize)

	# Define variables
	x = [pulp.LpVariable(f"x_{i}", lowBound = 0, cat = "Integer") for i in range(len(ind))]

	# int divider (product min step), example 1kg/20=50g
	divider = 20
	# Objective function: Minimize cost
	problem += pulp.lpSum(float(cen[i]) * x[i] / divider for i in range(len(ind)))

	# Constraints to meet nutritional requirements
	problem += pulp.lpSum(float(olb[i]) * x[i] / divider for i in range(len(ind))) >= norm_olb
	problem += pulp.lpSum(float(tau[i]) * x[i] / divider for i in range(len(ind))) >= norm_tau
	problem += pulp.lpSum(float(ogl[i]) * x[i] / divider for i in range(len(ind))) >= norm_ogl
	problem += pulp.lpSum(float(kal[i]) * x[i] / divider for i in range(len(ind))) >= norm_kca

	# limit on same products
	for i in range(len(x)):
		problem += x[i] <= 6

	# Constraints to not exceed the norm too much
	# cons=20
	# problem += pulp.lpSum(float(olb[i]) * x[i] / divider for i in range(len(ind))) <= norm_olb*cons
	# problem += pulp.lpSum(float(tau[i]) * x[i] / divider for i in range(len(ind))) <= norm_tau*cons
	# problem += pulp.lpSum(float(ogl[i]) * x[i] / divider for i in range(len(ind))) <= norm_ogl*cons
	# problem += pulp.lpSum(float(kal[i]) * x[i] / divider for i in range(len(ind))) <= norm_kca*cons

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
				solb += float(olb[i]) * var.varValue / divider
				stau += float(tau[i]) * var.varValue / divider
				sogl += float(ogl[i]) * var.varValue / divider
				skca += float(kal[i]) * var.varValue / divider
				if (safe_min(cenM[i]) < safe_min(cenR[i])):
					cena = cenM[i]
					site = saiM[i]
				else:
					cena = cenR[i]
					site = saiR[i]
				results["Edienkarte"].append(
					f"{name[i]} : {var.varValue / divider} {mer[i]} Cena:{cena} tīmekļa vietne: {site}")
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
