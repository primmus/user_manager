from flask import Blueprint, render_template, request, g
import user, tools

bp = Blueprint('disable', __name__, url_prefix='/disable')

@bp.route('/', methods=('POST', 'GET'))
def disableIndex():
    userToDisable = user.User()
    g.isSearch = True
    
    if request.method == 'POST':                
        g.isSearch = False
        if request.form['btn'] == 'Check':
            username = request.form['username']
            userToDisable = tools.getUser(username)        
        
            g.user = userToDisable
        elif request.form['btn'] == 'Disable':
            print('Disable user')

    return render_template('disable.html')