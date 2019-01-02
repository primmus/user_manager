import sqlite3
import schedule
import time
from apis import gsuite
import user
import tools


def deleteTask(taskId):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("DELETE FROM Tasks WHERE transfer_id=?", (taskId,))
        conn.commit()
        conn.close()


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
                status = gsuite.dataTransferChecker(row[4])
                if status == 'completed':
                        userToDelete = user.User()
                        userToDelete = tools.getUser(row[1])
                        gsuite.disableUser(userToDelete)
                        deleteTask(row[4])


def addAdmin(username, password):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        if c.execute('SELECT * FROM Users WHERE login = ?', (username,)).fetchone() is not None:
                conn.close()
                return 1
        else:
                c.execute("INSERT INTO Users (login, password) VALUES (?, ?)", (username, password))
                conn.commit()

        conn.close()
        return 0

def getAdmin(username):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        admin = c.execute('SELECT * FROM Users WHERE login = ?', (username,)).fetchone()
        return admin