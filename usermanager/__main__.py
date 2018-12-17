from flask import Flask, render_template, url_for
import threading
import apis.database

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

@app.route('/')
def index():
    return render_template('index.html')

import blueprints.user_search as user_search
app.register_blueprint(user_search.bp)

import blueprints.user_add as user_add
app.register_blueprint(user_add.bp)

import blueprints.user_disable as user_disable
app.register_blueprint(user_disable.bp)

import blueprints.login as login
app.register_blueprint(login.bp)

if __name__ == '__main__':
    monitorThread = threading.Thread(target=apis.database.startMonitor)
    #monitorThread.start()
    app.run(host='0.0.0.0', port=5000, debug=True) 