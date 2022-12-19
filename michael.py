from flask import Flask

app = Flask(__name__)

@app.route("/") 

def hello_world():

    file = open('return.txt','r')
    temp = file.read()
    file.close
    return temp
