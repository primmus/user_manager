from flask import Blueprint, render_template, request, session, redirect, url_for  # g

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=('POST', 'GET'))
def loginIndex():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']

        if login == 'sergio' and password == '1234':
            session.clear()
            session['user_id'] = 'rosca'

    return redirect(url_for('index'))