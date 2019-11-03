from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
import db

app = Flask(__name__)
APP_PARAMS = db.get_params()
APP_TABS = ["Dashboard", "Mutieren", "Konfiguration", "Vorerfassung"]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", app_params=APP_PARAMS, app_tabs=APP_TABS)


if __name__ == "__main__":
    app.run()
