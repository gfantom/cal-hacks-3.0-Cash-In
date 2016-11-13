from flask import Flask, render_template, request, url_for, redirect
import requests
from config import *
import urllib

auth_code = ""
access_token = ""
post_for_token = "https://connect.squareup.com/oauth2/token"
charge_url = "square-commerce-v1://payment/create?data="
fee = 0
event_label = ""

app = Flask(__name__)

@app.route("/")
def hello():
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return render_template("index.html")

@app.route("/eventpage")
def eventpage():
    return render_template("eventpage.html")

@app.route("/eventsetup")
def eventsetup():
    return render_template("eventsetup.html")

@app.route("/finishsetup")
def finishsetup():
    fee = float(request.args.get("fee"))
    event_label = request.args.get("label")
    return redirect(url_for("eventpage"))

@app.route("/charge")
def charge():
    data = {"amount_money": {"amount": fee, "currency_code": "USD"},
            "callback_url": "myapp-url-scheme://payment-complete",
            "client_id": APPLICATION_ID,
            "version": "1.1",
            "notes": event_label,
            "options": {"supported_tender_types": ["CREDIT_CARD","CASH"]},
            "clear_default_fees": True,
            "auto_return": True,
            "skip_receipt": True}
    return redirect(charge_url +
                    urllib.urlencode(data))
    

@app.route("/callback")
def callback():
    #if getting auth code...
    #auth_code = request.args.get("code")
    print("THE AUTH_CODE IS: " + auth_code)
    if request.args.get("code"):
        payload = {"client_id": APPLICATION_ID, "client_secret": APP_SECRET, "code": auth_code}
        response = requests.post(post_for_token, data=payload)
        access_token = response.headers["access_token"]
        return render_template("eventsetup.html")
    #if receiving data from a sent transaction...
    elif request.args.get("data"):
        return render_template("eventpage.html")
    
if __name__ == "__main__":
    app.run()
