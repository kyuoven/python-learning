from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from flask import request
from memeweb import functions
from memeweb.functions import Room

app = Flask(__name__)

urls = ("/", "show_room")


@app.route("/")
def index():
    session["room_name"] = functions.START
    return redirect(url_for("game"))


@app.route("/game", methods=["POST", "GET"])
def game():
    room_name = session.get("room_name")

    if request.method == "GET":
        if room_name:
            room = functions.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("you_died.html")

    else:
        action = request.form.get("action")

        if room_name and action:
            room = functions.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session["room_name"] = functions.name_room(room)
            else:
                session["room_name"] = functions.name_room(next_room)


app.secret_key = "b29530ca21b00a0a5ff3c505"

if __name__ == "__main__":
    app.run(debug=True)
