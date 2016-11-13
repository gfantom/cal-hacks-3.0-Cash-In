from flask import Flask, render_template
import requests
from config import *

auth_code = ""
access_token = ""
post_for_token = "https://connect.squareup.com/oauth2/token"

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login")
def login():
    return render_template("index.html")

@app.route("/eventpage")
def eventpage():
    return render_template("eventpage.html")

@app.route("/callback")
def callback():
    #if getting auth code...
    auth_code = requests.args.get("code")
    if requests.args.get("code"):
        payload = {"client_id": APPLICATION_ID, "client_secret": APP_SECRET, "code": auth_code}
        response = requests.post(post_for_token, data=payload)
        access_token = response.headers["access_token"]
        return render_template("eventsetup.html")
    #if receiving data from a sent transaction...
    elif requests.args.get("data"):
        return render_template("eventpage.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
