from flask import Flask, render_template, url_for

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    from . import user_search
    app.register_blueprint(user_search.bp)

    from . import user_add
    app.register_blueprint(user_add.bp)  

    return app