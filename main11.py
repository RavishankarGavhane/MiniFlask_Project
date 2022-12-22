"""
#############################################################################
TOPIC :
1. URL redirection using `redirect` function
2. API endpoint with form-data
3. Generating POST request from HTML form
4. Right click in chrome and inspect elements to see "network" actions
#############################################################################
"""


from flask import Flask, request, url_for, redirect


game = Flask(__name__)


@game.route("/success/<name>")
def success(name):
    return f"<h1> success - {name}</h1>"


@game.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        player = request.form.get("player")
        success_url = url_for("success", name=player)
        return redirect(success_url)

    return "<h1>DONE</h1>"


if __name__ == "__main__":
    game.run(debug=True)
