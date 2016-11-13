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

@app.route("/callback")
def callback():
    auth_code = requests.args.get("code")
    if auth_code != None:
        payload = {"client_id": APPLICATION_ID, "client_secret":
                   APP_SECRET, "code": auth_code}
        response = requests.post(post_for_token, data=payload)
        access_token = response.headers["access_token"]
    return render_template("partySetup.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
