# -*- coding: utf-8 -*-
from . import db


class Analyse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    column = db.Column(db.Enum(["Age", "Fare"]))
    metric = db.Column(db.Enum(["mean", "median", "min", "max"]))
    result = db.Column(db.Float)
    hist_file = db.Column(db.String(100))
    