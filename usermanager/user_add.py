from flask import Blueprint, render_template, request, g
from . import gsuite, activedirectory, user

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('/', methods=('POST', 'GET'))
def addIndex():
    if request.method == 'POST':
        newUser = user.User()
        newUser.firstName = request.form['firstName']
        newUser.lastName = request.form['lastName']
        newUser.login = request.form['userName']
        newUser.location = request.form['location']
        newUser.gEmailAliases = request.form.getlist('gEmailAliases')
        newUser.adServices = request.form.getlist('adServices')
        newUser.services = request.form.getlist('services')
        newUser.vpn = request.form.getlist('vpn')         

    return render_template('add.html')