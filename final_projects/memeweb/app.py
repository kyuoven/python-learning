from flask import Flask, session, redirect, request, escape, render_template, url_for
from memeweb import functions

# shutting down whatever activity on port:5000 (in terminal)  =
# lsof -i:5000
# kill "PID" (fill in the PID number attached to port:5000!!! it's not that hard :))

# assert helps detect problems early and works as documentation for other developers

# RENDER_TEMPLATES: Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the Jinja template library to render templates.
# URL_FOR: flask.url_for(endpoint, **values) Generates a URL to the given endpoint with the method provided.
# REDIRECT: redirecting to a specific URL (together with (url_for))

app = Flask(__name__)


@app.route("/")
def index():
    session["room_name"] = functions.START
    return redirect(url_for("game"))


@app.route("/game", methods=["GET", "POST"])
def game():
    room_name = session.get("room_name")
    if request.method == "GET":
        room = functions.load_room(room_name)
        return render_template("show_room.html", room=room)
    else:
        action = request.form.get("action")

        if room_name and action:
            room = functions.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session["room_name"] = functions.name_room(room)
            else:
                session["room_name"] = functions.name_room(next_room)

        return redirect(url_for("game"))


app.secret_key = "lpthw52"

if __name__ == "__main__":
    app.run(debug=True)
