import sqlite3
from datetime import time

CONN = sqlite3.connect('WorkTimeWatch.sqlite')
CURSOR = CONN.cursor()
print("Connection to sqlite3-database successfully established")


def get_params():
    ret = {}
    for key, value, type in CURSOR.execute("SELECT key, value, type FROM app_params"):
        casted_value = value
        if type == 'STRING':
            pass
        elif type == 'INTEGER':
            casted_value = int(value)
        elif type == 'TIME':
            hour, minute = value.split(":", 2)
            hour = int(hour)
            minute = int(minute)
            casted_value = time(hour=hour, minute=minute)

        ret[key] = casted_value

    return ret


if __name__ == "__main__":
    print(f"get_params(): {get_params()}")
