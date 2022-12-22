"""
#############################################################################
TOPIC :
1. path variables in URL
2. using path variables in function (view)
3. The path variables rules can be found here -
https://flask.palletsprojects.com/en/2.2.x/quickstart/#variable-rules
#############################################################################
flask --app main4 run
NOTE -
If you rename file name as either `main4.py` OR `wsgi.py`,
you can directly use `flask run`
1. PATH variable
example -
    <home-url>/addition/num1/num2
    here, num1 and num2 are path variables
    string:
    int:
    float:
    path:
    uuid:
2. query parameter
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1> hello world </h1>"


# <converter:variable_name>
@app.route("/addition/<int:num1>/<int:num2>")
def _add(num1, num2):
    result = num1 + num2
    return f"<h1>{result}</h1>"


@app.route("/about/<institute>")
def about(institute):
    print(type(institute))
    return f"<h1> handcrafted by Prashant - {institute}</h1>"


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
app.run(debug=True)

