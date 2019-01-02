import threading
import apis.database
from flask import Flask, render_template
from blueprints import user_search, user_add, user_disable, login, admin_user

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    ENABLED_USER_SETUP=False
)


@app.route('/')
def index():
    return render_template('index.html')


app.register_blueprint(user_search.bp)
app.register_blueprint(user_add.bp)
app.register_blueprint(user_disable.bp)
app.register_blueprint(login.bp)
app.register_blueprint(admin_user.bp)

if __name__ == '__main__':
    monitorThread = threading.Thread(target=apis.database.startMonitor)
    #monitorThread.start()
    app.run(host='0.0.0.0', port=5000, debug=True)
