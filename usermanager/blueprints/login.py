from flask import (Blueprint, render_template, request,
                   session, redirect, url_for, g)  # current_app)
from werkzeug.security import check_password_hash, generate_password_hash
from apis import database
import functools
import json

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=('POST', 'GET'))
def loginIndex():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']

        admin = database.getAdmin(login)

        if check_password_hash(admin[2], password):
                session.clear()
                session['user_id'] = admin[1]
                g.admin = admin[1]
                return redirect(url_for('index'))

        else:
                return 'Login error', 403

    return render_template('login.html')

@bp.route('/admin', methods=('POST', 'GET'))
def adminIndex():

    admin_page_enabled = json.loads(open('settings.json').read())['admin_page']
    if not admin_page_enabled:
        return 'Admin page disabled', 202

    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']
        response = database.addAdmin(login, generate_password_hash(password))
        if response == 1:
                return 'User already exists', 500
        else:
                return redirect(url_for('login.loginIndex'))

    return render_template('admin.html')


def login_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
                if session.get('user_id') is None:
                        return redirect(url_for('login.loginIndex'))

                return view(**kwargs)
        return wrapped_view


@bp.route('/logout')
def logout():
        session.clear()
        return redirect(url_for('index'))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.isLogged = False
    else:
        g.isLogged = True
