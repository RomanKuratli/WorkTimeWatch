import sqlite3
from datetime import time, date, datetime

CONN = sqlite3.connect('WorkTimeWatch.sqlite')
CURSOR = CONN.cursor()
print("Connection to sqlite3-database successfully established")

# ====== PARAMS ========
def get_table_app_params():
    cur = sqlite3.connect('WorkTimeWatch.sqlite').cursor()
    return [
        {"key": key, "value": value, "type": param_type}
        for key, value, param_type in cur.execute("SELECT key, value, type FROM app_params")
    ]


def get_params():
    ret = {}
    cur = sqlite3.connect('WorkTimeWatch.sqlite').cursor()
    for key, value, param_type in cur.execute("SELECT key, value, type FROM app_params"):
        casted_value = value
        if param_type == 'STRING':
            pass
        elif param_type == 'INTEGER':
            casted_value = int(value)
        elif param_type == 'TIME':
            hour, minute = value.split(":", 2)
            hour = int(hour)
            minute = int(minute)
            casted_value = time(hour=hour, minute=minute)
        ret[key] = casted_value
    return ret

def post_params(body): 
    for key, value in body.items():
        conn = sqlite3.connect('WorkTimeWatch.sqlite')
        cur = conn.cursor()
        cur.execute("UPDATE app_params SET value = ? WHERE key = ?", (value, key))
        conn.commit()

# === END PARAMS ========
# ====== WORKING TIME ========
def exists_working_time_entry(date):
    conn = sqlite3.connect('WorkTimeWatch.sqlite')
    cur = conn.cursor()
    for key, value, param_type in cur.execute("SELECT dt FROM working_time WHERE dt = ?", (date,)):
        return True
    return False


def insert_working_time(date, vm_start, vm_end, nm_start, nm_end):
    vm_time = datetime.combine(date.min, vm_end) - datetime.combine(date.min, vm_start)
    nm_time = datetime.combine(date.min, nm_end) - datetime.combine(date.min, nm_start)
    total_time = vm_time + nm_time
    conn = sqlite3.connect('WorkTimeWatch.sqlite')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO working_time VALUES (?, ?, ?, ?, ?, ?)",
        (date, vm_start, vm_end, nm_start, nm_end, total_time)
    )
    conn.commit()


def update_working_time(date, vm_start, vm_end, nm_start, nm_end):
    total_time = (vm_end - vm_start) + (nm_end - nm_start)
    conn = sqlite3.connect('WorkTimeWatch.sqlite')
    cur = conn.cursor()
    cur.execute(
        "UPDATE working_time SET vm_start = ?, vm_end = ?, nm_start = ?, nm_end = ?, total_time = ? WHERE dt = ?",
        (vm_start, vm_end, nm_start, nm_end, total_time, date)
    )
    conn.commit()
# === END WORKING TIME ========

if __name__ == "__main__":
    print(f"get_params(): {get_params()}")
