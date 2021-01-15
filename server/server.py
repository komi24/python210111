# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request
import pandas as pd
from uuid import uuid4
import matplotlib.pyplot as plt

from models import db
from models.Analyse import Analyse


app = Flask(__name__, static_folder="uploads", static_url_path="/uploads")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///analysis.sqlite3"
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

with app.app_context():
    db.init_app(app)
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return "Mes contacts"

@app.route("/execute", methods=["POST"])
def execute():
    firstname = request.form.get("first_name")
    lastname = request.form.get("last_name")
    telephone = request.form.get("tel")
    metric = request.form.get("metric", "mean") 
    column = request.form.get("column", "Age")
    file = request.files["file"]

    # file.save(os.path.join(app.config["UPLOAD_FOLDER"],"file.csv"))    
    # df = pd.read_csv(os.path.join(app.config["UPLOAD_FOLDER"],"file.csv"))
    
    stream = file.stream
    df = pd.read_csv(stream)
    
    df[column].hist()
    hist_file = str(uuid4()) + ".png"
    plt.savefig(os.path.join(app.config["UPLOAD_FOLDER"],hist_file))
    result = getattr(pd.Series, metric)(df[column])
    
    analyse = Analyse(
        firstname=firstname,
        lastname=lastname,
        metric=metric,
        column=column,
        result=result,
        hist_file=hist_file
    )
    db.session.add(analyse)
    db.session.commit()
    
    return render_template("index.html", resultat=result, hist_file=hist_file)


app.run(port=8080, debug=True)
