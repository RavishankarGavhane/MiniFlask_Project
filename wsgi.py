"""
TOPICS
1. `APP` instantiation and related attributes
2. `Rendering templates
3. Intro to JINJA templates basics
4. We can include variables and expression inside HTML using following
    delimiters
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index(name="world"):
    print(f"{__name__} running")
    return render_template("hello-world.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
