"""
Flask app to host my sample BIO
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    "My BIO home"
    return "Shiva"


#------Start of the scritp
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6464)