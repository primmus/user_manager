import sqlite3
import schedule
import time
from apis import gsuite


def addTask(taskId, originUser, destinationUser):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("INSERT INTO Tasks (origin_user, destination_user, time_stamp, transfer_id) VALUES (?, ?, DATETIME('now'), ?)", (originUser.login, destinationUser.login, taskId))
        conn.commit()
        conn.close()


def startMonitor():
    print("Task monitor started")
    schedule.every(120).seconds.do(dataTransferMonitorJob)
    while True:
        schedule.run_pending()
        time.sleep(1)


def dataTransferMonitorJob():
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("SELECT * FROM Tasks")
        rows = c.fetchall()
        conn.close()
        for row in rows:
                gsuite.dataTransferChecker(row[4])
