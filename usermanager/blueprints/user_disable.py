from flask import Blueprint, render_template, request, g
import tools
import apis
import user

bp = Blueprint('disable', __name__, url_prefix='/disable')

userToDisable = user.User()


@bp.route('/', methods=('POST', 'GET'))
def disableIndex():
    g.isSearch = True

    if request.method == 'POST':
        g.isSearch = False
        if request.form['btn'] == 'Check':
            username = request.form['username']
            global userToDisable
            userToDisable = tools.getUser(username)
            g.user = userToDisable
        elif request.form['btn'] == 'Disable':
            if 'yes' in request.form.getlist('dataTransfer'):
                destinationUsername = request.form['destinationUser']
                destinationUser = tools.getUser(destinationUsername)
                apis.gsuite.dataTransfer(userToDisable, destinationUser)
            else:
                apis.gsuite.disableUser(userToDisable)

    return render_template('disable.html')
