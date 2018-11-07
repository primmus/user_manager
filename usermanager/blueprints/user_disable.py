from flask import Blueprint, render_template, request, g
import user, tools

bp = Blueprint('disable', __name__, url_prefix='/disable')

@bp.route('/', methods=('POST', 'GET'))
def disableIndex():
    userToDisable = user.User()
    
    if request.method == 'POST':                
        username = request.form['username']
        userToDisable = tools.getUser(username)        
        
        g.user = userToDisable        

    return render_template('disable.html')