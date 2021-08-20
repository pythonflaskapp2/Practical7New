
from flask import Flask, jsonify,render_template,Request
from flask.globals import request
from jinja2 import exceptions
import json
from model.User import User



app=Flask(__name__) 


@app.route('/')
def index():
    return "<h1>Welcome to Python Flask Heroku App!!</h1>"


@app.route('/users',methods = ["GET"])

def getUsers():
        try:
            users = User.getUsers()
            output ={"Users":users}

            return jsonify(output),200
        except Exception as err:
            print(err)
            output = {"Message":"Error occurred"}
            return jsonify(output),500


   


if __name__ == '__main__':
    app.run(debug=True) #start the flask app with default port 5000
