from flask import Flask, render_template, abort 
from datetime import datetime
from model import db

app= Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html", message="Here's a message from the view"
    )

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

@app.route("/card")
def card_view():
    #try: 
        card = db[0]
        return render_template("card.html", card=card)
   # except IndexError: 
    #    return(404)

#add how many times this page was viewed
#counter =0
#@app.route("/counter")
#def count():
#    global counter
#    counter += 1
#    return "this page was viewed :" + str(counter) + " times"