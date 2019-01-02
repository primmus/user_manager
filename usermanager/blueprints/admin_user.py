from flask import Blueprint, render_template, request, g, session, redirect
from apis import activedirectory  # gsuite
import user
from blueprints.login import login_required

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/', methods=('POST', 'GET'))
def adminIndex():    

    return 'OK', 200
