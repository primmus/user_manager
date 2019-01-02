from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, session, redirect, url_for  # g
import functools

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=('POST', 'GET'))
def loginIndex():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']        

        # TODO: replace this for the DB search
        if login == 'sergio' and password == '1234':
            session.clear()
            session['user_id'] = 'rosca'

    return render_template('login.html')

def login_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
                print(session.get('user_id'))
                if session.get('user_id') is None:
                        print('Is None!')
                        return redirect(url_for('login.loginIndex'))

                return view(**kwargs)
        return wrapped_view