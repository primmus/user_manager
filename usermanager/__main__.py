from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

import blueprints.user_search as user_search
app.register_blueprint(user_search.bp)

import blueprints.user_add as user_add
app.register_blueprint(user_add.bp)

import blueprints.user_disable as user_disable
app.register_blueprint(user_disable.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)