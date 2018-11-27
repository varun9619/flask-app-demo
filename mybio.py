"""
Flask app to host my sample BIO
"""
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    "My BIO home"
    return render_template("index.html")


#------Start of the scritp
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6464)