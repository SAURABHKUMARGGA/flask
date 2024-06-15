import flask
from markupsafe import escape
# print(__name__)
myflask = flask
app = myflask.Flask(__name__)

@app.route("/")
@app.route("/<string:name>")
def index(name=None):
    return myflask.render_template("index.html",person=name)

@app.route("/hello")
def hello():
    return "<p>Hello i am saurabh kumar.</p>"


name = "saurabh kuamr"


@app.route("/photos")
def photos():
    return f"my name is {name}"   


@app.route("/user/<name>")
def user(name):
    return f"you name is {escape(name)}"

@app.route("/num/<int:age>")
def showAge(age):
    return f"you age is {escape(age)}"

@app.route("/path/<path:subpath>")
def path(subpath):
    return f"path is {escape(subpath)}"


if __name__=="__main__":
    app.run(debug=True)