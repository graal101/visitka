#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сайт визитка для учебы и практики. Для Gita."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
