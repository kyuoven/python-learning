from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from flask import request
import memeweb

app = Flask(__name__)


@app.route("/")
def index():
    session["room_name"] = memeweb.START
    return redirect(url_for("game"))


@app.route("/game")
def game():
    room_name = session.get("room_name")

    if request.method == "GET":
        if room_name:
            room = memeweb.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("you_died.html")

    else:
        action = request.form.get("action")

        if room_name and action:
            room = memeweb.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session["room_name"] = memeweb.name_room(room)
            else:
                session["room_name"] = memeweb.name_room(next_room)

        return redirect(url_for("game"))


app.secret_key = "b'%}e|\x9bq\xfaEsS\x9f\xef"
