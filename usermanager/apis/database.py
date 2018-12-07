import sqlite3
import schedule
import time

def startMonitor():
    print("Task monitor started")
    schedule.every(10).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

def job():
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        origin_id = '"foo"'
        destination_id = '"bar"'        

        c.execute("INSERT INTO Tasks (origin_id, destination_id, timestamp) VALUES ({}, {}, DATETIME('now'))".format(origin_id, destination_id))

        conn.commit()
        conn.close()
        print('Done')
    