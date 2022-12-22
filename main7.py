"""
#############################################################################
TOPIC :
1. path variables in URL
2. using path variables in function (view)
3. The path variables rules can be found here -
https://flask.palletsprojects.com/en/2.2.x/quickstart/#variable-rules
#############################################################################
Example URLs in this application -
/user/prashant
/post/1234
/path/subpath1/subpath2/subpath3
"""

from flask import Flask


app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {subpath}'
app.run(debug=True)
