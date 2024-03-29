from flask import Blueprint, render_template, request, g  # session, redirect
from apis import activedirectory  # gsuite
import user
from blueprints.login import login_required

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('/', methods=('POST', 'GET'))
@login_required
def addIndex():

    if request.method == 'POST':
        newUser = user.User()
        newUser.firstName = request.form['firstName']
        newUser.lastName = request.form['lastName']
        newUser.login = request.form['userName']
        newUser.location = request.form['location']
        newUser.gEmailAliases = request.form.getlist('gEmailAliases')
        newUser.adGroups = request.form.getlist('adGroups')
        newUser.services = request.form.getlist('services')
        newUser.vpn = request.form.getlist('vpn')        

    adGroups = activedirectory.getGroups()
    g.adGroups = adGroups

    return render_template('add.html')
