from flask import Blueprint, render_template, request, g
from . import gsuite, activedirectory

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('/', methods=('POST', 'GET'))
def addIndex():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        userName = request.form['userName']
        location = request.form['location']
        aliases = request.form.getlist('aliases')
        schibstedServices = request.form.getlist('schibstedServices')
        services = request.form.getlist('services')
        vpn = request.form.getlist('vpn')

        print('Creating a new login {} for {} {}  in {} with the following access:'.format(userName, firstName, lastName, location))
        print('Schibsted services: {}'.format(schibstedServices))
        print('Corporate services: {}'.format(services))
        print('VPN access: {}'.format(vpn))
        print('Adding email aliases: {}'.format(aliases))     

    return render_template('add.html')