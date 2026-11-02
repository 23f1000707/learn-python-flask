'''
File 2
Flask app dev
Author  : Jayhari Patel
Version : v1

Description:
    GET api with the json data
'''

# import the flask lib
from flask import Flask, jsonify


# create a app
app = Flask(__name__)


# define the api route and api call method
@app.route('/api/hello', methods=['GET'])
def helloWorld():
    data = {
        "message" : "hello world!!! welcome to file 2."
    }
    return jsonify(data), 200


# do addition by passing data on api
@app.route('/api/add/<int:a>/<int:b>', methods=['GET'])
def addition_by_api(a, b):
    sum = a + b
    data = {
        "message" : "Addition methods by api data",
        "Args" : f"a: {a}, b: {b}",
        "sum" : sum 
    }
    return jsonify(data), 200


# script entry point
if __name__ == '__main__':
    app.run(debug=True)

