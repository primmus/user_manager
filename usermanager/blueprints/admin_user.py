from flask import Blueprint, render_template, request, g, session, redirect
from flask import current_app as app
from apis import activedirectory  # gsuite
import user
from blueprints.login import login_required

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/', methods=('POST', 'GET'))
def adminIndex():

    if app.config['ENABLED_USER_SETUP']:
        return 'OK', 200
    else:
        return 'Admin page disabled', 202