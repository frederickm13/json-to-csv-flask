import os
import processors
from flask import Flask, jsonify, redirect, render_template, request
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/JsonToCsv", methods=["POST"])
def JsonToCsv():
    return processors.JsonToCsvProcessor(request)


@app.route("/CsvToJson", methods=["POST"])
def CsvToJson():
    return processors.CsvToJsonProcessor(request)