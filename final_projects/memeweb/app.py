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
    room = functions.load_room("start_room")
    return render_template("show_room.html", room=room)


@app.route("/game", methods=["POST"])
def post_game():
    action = request.form.get(action)
    # passing the html templaate and showing what to show the user????
    userinput = request.form.get("userinput")
    if userinput is None:
        # if there is no userinput
        return render_template("empty.html", room=room)
    elif userinput == "*":
        room = functions.run()
        return render_template("show_room.html", room=room), redirect(
            url_for(post_game)
        )


app.secret_key = "lpthw52"

if __name__ == "__main__":
    app.run(debug=True)
