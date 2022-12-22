from flask import Flask, url_for


# Flask` is the class we use to instantiate an application.
app = Flask(__name__)


@app.route('/')
def index():
    print(f"{__name__} running")
    return 'index'


@app.route('/login')
def login(next=""):
    print(next)
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

    app.run(debug=True)
