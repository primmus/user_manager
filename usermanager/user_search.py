from flask import Blueprint, render_template, request, g
from . import gsuite

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/', methods=('POST', 'GET'))
def searchIndex():
    g.google = None
    if request.method == 'POST':
        username = request.form['username']
        if '@' in username:
            username = username.split('@')[0]
        email = username + '@distilled.ie'      
        
        g.google = gsuite.searchUser(email)       

    return render_template('search.html')