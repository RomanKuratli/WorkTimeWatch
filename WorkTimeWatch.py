from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
import db
import csv
from datetime import datetime, time, date


app = Flask(__name__)
APP_PARAMS = db.get_params()
APP_TABS = ["Dashboard", "Mutieren", "Konfiguration", "Vorerfassung"]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.jinja", app_params=APP_PARAMS, app_tabs=APP_TABS)


# ====== PARAMS ========
@app.route("/params", methods=["GET"])
def get_params():
    return jsonify(db.get_table_app_params())


@app.route("/params", methods=["POST"])
def post_params():
    global APP_PARAMS
    print("POST: /params aufgerufen")
    body = request.get_json(force=True)
    print("body:", body)
    db.post_params(body)
    # reload app params
    APP_PARAMS = db.get_params()
    return jsonify({'msg': 'Application parameters successfully changed!'})
# ====== END PARAMS ========


# ====== WORKING TIME ========
@app.route("/working_time", methods=["POST"])
def post_working_time():
    print("POST: /working_time aufgerufen")
    body = request.get_json(force=True)
    print("body:", body)
    db.insert_working_time(body["DT"], body["VM_START"], body["VM_END"], body["NM_START"], body["NM_END"])
    return jsonify({'msg': 'Working time successfully inserted!'})


@app.route("/working_time", methods=["PUT"])
def put_working_time():
    print("POST: /working_time aufgerufen")
    body = request.get_json(force=True)
    print("body:", body)
    db.update_working_time(body["DT"], body["VM_START"], body["VM_END"], body["NM_START"], body["NM_END"])
    return jsonify({'msg': 'Working time successfully inserted!'})


def str_to_time(str_val):
    tokens = str_val.split(':')
    return time(hour=int(tokens[0]), minute=int(tokens[1]))


@app.route('/upload_times_csv', methods=["POST"])
def upload_times_csv():
    # split csv file in lines
    for line in request.get_data().decode("utf-8").splitlines():
        if not 'DT;' in line:
            fields = line.split(sep=';')
            dt = datetime.strptime(fields[0], '%d.%m.%y')
            vm_start = str_to_time(fields[1])
            vm_end = str_to_time(fields[2])
            nm_start = str_to_time(fields[3])
            nm_end = str_to_time(fields[4])

            if db.exists_working_time_entry(dt):
                db.update_working_time(dt, vm_start, vm_end, nm_start, nm_end)
            else:
                db.insert_working_time(dt, vm_start, vm_end, nm_start, nm_end)
    return jsonify({'msg': 'CSV file successfully uploaded!'})
# ====== END WORKING TIME ========

if __name__ == "__main__":
    app.run()
