from flask import Blueprint, render_template, request, g, session

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/', methods=('POST', 'GET'))
def addIndex():
    return render_template('login.html')