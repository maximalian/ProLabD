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

	# Call the calculate_diet function with the user inputs and store the result
	results = DIETcalc.calculate_diet(age, height, weight, gender)  # Call the function with inputs

	if results:
		# Render the result.html template with the calculation results
		return render_template('result.html', results = results)
	else:
		return "An error occurred during the calculation."


if __name__ == '__main__':
	# Run the Flask application on the specified host and port
	app.run("0.0.0.0", port = 443, debug = True)
