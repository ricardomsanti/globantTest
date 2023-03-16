from flask import Flask
import os
from datetime import datetime as dt 
from localWorks import LocalOrigin as lo
from flask import jsonify

app = Flask(__name__)

###############################################################################
#API
###############################################################################


@app.route(route='/scan_origin', methods=["GET"])
def scan_origin():
    files = {"sdsd":"kkjiji"} 
    return jsonify(files)

"""
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }"""


#starting the server
#FLASK_APP=main.py
#flask run
