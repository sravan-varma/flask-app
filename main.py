# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
from additon_function import add
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/',methods=["GET"])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Welcome to my WebPage'


@app.route('/shopping',methods=["GET"])
# ‘/’ URL is bound with hello_world() function.
def hello_world1():
	return 'shopping page'

@app.route('/cart',methods=["GET"])
# ‘/’ URL is bound with hello_world() function.
def hello_world2():
	return 'cart page'


# Endpoint to create a new guide
@app.route('/guide', methods=["POST"])
def display():
    title = request.json['name']
    content = request.json['age']
    return f"My name is {title} with age {content}"

@app.route('/addition', methods=["POST"])
def addition():
    numbers = request.json['numbers']
    result = add(*numbers)
    return f"sum of the numbers is {result}"

# main driver functi


if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(host="0.0.0.0",port=5000)
