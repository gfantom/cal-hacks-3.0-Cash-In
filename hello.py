from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login")
def login():
	return render_template("index.html")

@app.route("/callback")
def callback():
    

if __name__ == "__main__":
    app.run()
