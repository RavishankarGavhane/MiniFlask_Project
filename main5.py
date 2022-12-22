"""
# how to run your application in debug mode?
flask --app <file-name> --debug run
"""

import json
from flask import Flask, request


app = Flask(__name__)


class MyDB:
    """
    class that is runtime DB.
    NOTE - this DB persists data as long as app is running
    """

    foo = []


@app.get("/data")
def get_data():
    """
    HTTP GET request from postman/ browser
    Returns:
        HTML data string
    """
    return f"<h1> data available - {MyDB.foo}</h1>"


@app.post("/data")
def post_data():
    """
    HTTP POST request with JSON payload
    Returns:
        HTML data string
    Example -
    1. Go to postman
    2. change HTTP request type to POST
    3. go to "body" tab and add dict-like data
    4. select radio button called "raw" and then select "json" from dropdown
    5. execute
    """
    body = request.data  # byte-string
    data_ = json.loads(body)  # serializing byte-string into `dict`
    for value_ in data_.values():
        MyDB.foo.append(value_)
    return f"<h1> latest data {MyDB.foo} </h1>"


if __name__ == "__main__":
    print("hello world")
    app.run(debug=True)

