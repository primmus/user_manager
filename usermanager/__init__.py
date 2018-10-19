from flask import Flask

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return '<h1>Index page</h1>'

    from . import user_search
    app.register_blueprint(user_search.bp)  

    return app