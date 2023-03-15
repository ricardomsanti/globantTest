#basic api structure
#%%
from flask import Flask
import os
from datetime import datetime as dt 
app = Flask(__name__)

def write_to():
        print("feito")


@app.route('/hello')
def hello():
    with open("D://GIT_CODE//GLOBANT//globantTest//testing//testaa.txt", "a", encoding="utf-8") as file:
        t = str(dt.now())
        file.write(t)
    return 'Hello, World!'
    print("kmkm")


#starting the server
#FLASK_APP=api.py
#flask run

"""
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['a.txt']
        f.save('/var/www/uploads/uploaded_file.txt')
"""

from globanttest.codwe
