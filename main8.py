"""
MVC => (Model - View - Control)
MVT => (Model - Template - View)
In terms of flask
Model - `data_models`
View - `templates`
Control - `saving_account`, `current_account`
Model => Database related part (data structure, DDL)
project root (swapi)
    model
        character
        film
        species
    view (front end)
        html (building web pages)
        css (styling)
        php
        javascript
    control (business logic)
        student
        pensioner
        saving
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
def hello():
    return render_template("hello.html")
app.run(debug=True)
