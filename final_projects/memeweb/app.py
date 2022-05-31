from flask import Flask, session, redirect, request, render_template, url_for, escape
from memeweb import functions
from memeweb.functions import Room
import web

# assert helps detect problems early and works as documentation for other developers

app = Flask(__name__)


@app.route("/")
def index():
    error = None
    session["room_name"] = functions.START
    return redirect(url_for("game"))


@app.route("/game", methods=["GET", "POST"])
def game():
    room_name = session.get("room_name")

    if request.method == "GET":
        if room_name:
            room = functions.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("show_room.html", room=room)

    if request.method == "POST":
        


app.secret_key = "b29530ca21b00a0a5ff3c505"

if __name__ == "__main__":
    app.run(debug=True)
