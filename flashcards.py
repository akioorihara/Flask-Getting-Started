from flask import Flask
from datetime import datetime

app= Flask(__name__)

@app.route("/")
def welcome():
    return "welcome!"


@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

#add how many times this page was viewed
counter =0
@app.route("/counter")
def count():
    global counter
    counter += 1
    return "this page was viewed :" + str(counter) + " times"