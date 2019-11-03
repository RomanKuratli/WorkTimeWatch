from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
import db

app = Flask(__name__)
APP_PARAMS = db.get_params()
APP_TABS = ["Dashboard", "Mutieren", "Konfiguration", "Vorerfassung"]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.jinja", app_params=APP_PARAMS, app_tabs=APP_TABS)


@app.route("/params", methods=["GET"])
def get_params():
    return jsonify(db.get_table_app_params())


@app.route("/params", methods=["POST"])
def post_params():
    print('POST: /params aufgerufen')
    return jsonify({'msg': 'Application parameters successfully changed!'})


if __name__ == "__main__":
    app.run()
