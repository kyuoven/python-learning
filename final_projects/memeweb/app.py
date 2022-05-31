from flask import Flask, session, redirect, request, render_template, url_for
from memeweb import functions
from memeweb.functions import Room
import web

# shutting down whatever activity on port:5000 (in terminal)  =
# lsof -i:5000
# kill "PID" (fill in the PID number attached to port:5000!!! it's not that hard :))

# assert helps detect problems early and works as documentation for other developers

app = Flask(__name__)


@app.route("/")
def index():
    error = None
    session["room_name"] = functions.START
    return redirect(url_for("get_game"))


@app.route("/game", methods=["GET"])
def get_game():
    room_name = session.get("room_name")
    # posting the html template to accept submissions
    if request.method == "GET":
        if room_name:
            room = functions.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return redirect(url_for("get_game"))


@app.route("/game", methods=["POST"])
def post_game():
    userinput = request.form.get("userinput")
    if userinput is None:
        # no user input
        return render_template("you_died.html")
    room_name = session.get(room_name)
    # passing the html templaate and showing what to show the user????
    if request.method == "POST":
        room = functions.load_room("show_room.html")
        return render_template("show_room.html")
    else:
        return redirect(url_for("post_game"))


app.secret_key = "lpthw52"

if __name__ == "__main__":
    app.run(debug=True)
