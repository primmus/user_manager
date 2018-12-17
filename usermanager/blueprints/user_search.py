from flask import Blueprint, render_template, request, g, session, redirect, url_for
import user, tools

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/', methods=('POST', 'GET'))
def searchIndex():    

    if session['user_id'] != 'rosca':
        return redirect(url_for('login.loginIndex'))

    userToSearch = user.User()
    g.user = user.User()
    
    if request.method == 'POST':        
        username = request.form['username']        
        userToSearch = tools.getUser(username)        
        
        g.user = userToSearch        

    return render_template('search.html')