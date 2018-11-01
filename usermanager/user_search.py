from flask import Blueprint, render_template, request, g
from . import gsuite, activedirectory, user

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/', methods=('POST', 'GET'))
def searchIndex():
    userToSearch = user.User()
    g.user = user.User()
    
    if request.method == 'POST':        
        username = request.form['username']
        if '@' in username:
            username = username.split('@')[0]
        email = username + '@distilled.ie'
        userToSearch.login = username
        userToSearch.email = email

        userToSearch = gsuite.searchUser(userToSearch)
        userToSearch = activedirectory.getUser(userToSearch)
        
        g.user = userToSearch        

    return render_template('search.html')