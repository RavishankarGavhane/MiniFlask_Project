"""
#############################################################################
TOPIC :
1. URL redirection using `redirect` function
2. getting URL binding for a particular function using `url_for` function
#############################################################################
localhost:8080/api/starships
redirect - localhost:8080/api/login
users
    manager
    client
    employee
"""


from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route("/manager")
def greet_manager():
    url = url_for("greet_employee", name="prashant")
    print(url)
    return "<h1>manager:: Good morning</h1>"


@app.route("/employee/<name>")
def greet_employee(name):
    return f"<h1>employee:: good morning, {name}</h1>"


@app.route("/client/<client>")
def greet_client(client):
    return f"<h1>client:: good morning, {client}</h1>"


@app.route("/user/<use_type>/<name_>")
def greet_everyone(use_type, name_):
    if use_type == "employee":
        emp_url = url_for("greet_employee", name=name_)
        return redirect(emp_url)
    elif use_type == "client":
        client_url = url_for("greet_client", client=name_)
        return redirect(client_url)
    return f"<h1>choose either employee or client</h1>"


if __name__ == "__main__":
    app.run(debug=True)
