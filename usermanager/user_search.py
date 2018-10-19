from flask import Blueprint, render_template, request, g
from . import gsuite

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/', methods=('POST', 'GET'))
def searchIndex():
    g.google = None
    if request.method == 'POST':
        g.google = gsuite.searchUser(request.form['username'])        

    return render_template('search.html')