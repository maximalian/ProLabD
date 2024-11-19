from flask import Flask, request, render_template

import DIETcalc  # Import the modified DIETcalc that has the calculate_diet function

app = Flask(__name__)


# Initialize the Flask application

@app.route('/')
def index():
	"""
	Route for the homepage which renders the index.html template.
	This template should contain the input form for user data.
	"""
	return render_template('index.html')  # Create this template to have the input form


@app.route('/calculate', methods = ['POST'])
def calculate():
	"""
	    Route for handling form submission from index.html.
	    It extracts user data from the form and calls the calculate_diet function from DIETcalc module.
	    The result is then rendered in the result.html template.
	"""
	age = float(request.form['age'])
	height = float(request.form['height'])
	weight = float(request.form['weight'])
	gender = request.form['gender']
	if gender == 'man':
		gender = 1
	else:
		gender = 0

	categories = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']
	checkbox_values={category: False for category in categories}
	checked_categories = request.form.getlist('category')
	for category in checked_categories:
		if category in checkbox_values:
			checkbox_values[category] = True
	checkbox_array = [checkbox_values[category] for category in categories]

	productType = request.form['type']
	veganCheck = request.form.get('vegan')
	vegan = 0
	if veganCheck == 'vegan':
		vegan = 1
	Type = 0
	if productType == 'Select categories':
		Type = 1


	# Call the calculate_diet function with the user inputs and store the result
	results = DIETcalc.calculate_diet(age, height, weight, gender,vegan,Type,checkbox_array)  # Call the function with inputs
	if results:
		# Render the result.html template with the calculation results
		return render_template('result.html', results = results)
	else:
		return "An error occurred during the calculation."


if __name__ == '__main__':
	# Run the Flask application on the specified host and port
	app.run("0.0.0.0", port = 5001, debug = True)
