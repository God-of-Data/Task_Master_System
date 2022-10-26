
from flask import Flask, redirect

from user.routes import user
from tasks.routes import tasks


app = Flask(__name__)

app.secret_key = b'\xa4\x93\xdc\xc4\x96\x81\x11f\x85G\xf1Q\xb0=&\x92'

app.register_blueprint(user)
app.register_blueprint(tasks)


@app.route("/")
def index():

    return redirect("/user/signin/")
