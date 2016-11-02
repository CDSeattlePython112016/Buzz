from flask import Flask, render_template, request	
app = Flask(__name__)

@app.route('/')
def survey():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	print request.form
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	location = request.form['location']
	language = request.form['language']
	return render_template('surveyA.html', firstname=firstname, lastname=lastname, location=location, language=language)

app.run(debug=True)