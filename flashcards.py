from flask import (Flask, render_template, abort, jsonify, request, redirect, url_for)
from datetime import datetime
from model import db

app= Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html", cards=db
    )

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

@app.route("/add_card")
def add_card():
    if request.method == 'POST':
    #form submits, process data 
        card = {"question":request.form['question'],
                "answer": request.form['answer']}
        db.append(card)

    else: 
        return render_template('add_card.html')


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)

@app.route("/api/card/")
def api_card_list():
    return jsonify(db)

@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)