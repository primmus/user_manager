from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

import user_search
app.register_blueprint(user_search.bp)

import user_add
app.register_blueprint(user_add.bp)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)