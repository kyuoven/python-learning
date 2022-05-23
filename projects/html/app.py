from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    greeting = render_template("html_tryout.html")
    return render_template("html_tryout.html", greeting=greeting)


if __name__ == "__main__":
    app.run()
