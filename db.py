import sqlite3
from datetime import time

CONN = sqlite3.connect('WorkTimeWatch.sqlite')
CURSOR = CONN.cursor()
print("Connection to sqlite3-database successfully established")


def get_cursor():
    return sqlite3.connect('WorkTimeWatch.sqlite').cursor()


def get_table_app_params():
    c = get_cursor()
    return [
        {"key": key, "value": value, "type": param_type}
        for key, value, param_type in c.execute("SELECT key, value, type FROM app_params")
    ]


def get_params():
    ret = {}
    c = get_cursor()
    for key, value, param_type in c.execute("SELECT key, value, type FROM app_params"):
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


if __name__ == "__main__":
    print(f"get_params(): {get_params()}")
