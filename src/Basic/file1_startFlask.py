'''
File 1
Start with the Flask app dev
Author  : Jayhari Patel
Version : v1

Description:
    Create a flask script and verify it how the API is working
'''

# import the flask lib
from flask import Flask


# create a app
app = Flask(__name__)


# define the api route and api call method
@app.route('/api/hello', methods=['GET'])
def helloWorld():
    return 'hello world!!! welcome to file 1.', 200

# script entry point
if __name__ == '__main__':
    app.run(debug=True)

