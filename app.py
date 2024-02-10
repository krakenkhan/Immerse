from cs50 import sql
from flask import Flask, flash,jsonify, redirect, render_template, request, session
from flask_session import Session
import json

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == "POST":
        words = request.form.get("text")
        l = len(words)
        if words[l-1] != "." or words[l-1] != "?" or words[l-1] != "!" or words[l-1] != " ":
            words+="."
        texts=[]
        s=""
        for text in words:
            s = s+text
            if text ==" " or text == "." or text == "?" or text == "!":
                texts.append(s)
                s=""
        return render_template("read.html", texts=texts)
    else:
        return render_template("index.html")
