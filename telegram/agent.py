import db_operations as db
import operations as op
from datetime import datetime
import time
import pytz


def main():
    start_time = datetime.utcnow().replace(tzinfo=pytz.utc)
    time.sleep(10)
    tasks = db.active()
    for task in tasks:
        temp = task[5]
        new_requests = start_time < temp
        if new_requests:
            op.send_to_all(task)


if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            print("Всё хуйня")
