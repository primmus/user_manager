from flask import Blueprint, render_template, request, g
from . import gsuite, activedirectory

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('/', methods=('POST', 'GET'))
def addIndex():
    
        

    return render_template('add.html')