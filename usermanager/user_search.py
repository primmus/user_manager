from flask import Blueprint, render_template, request, g

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/', methods=('POST', 'GET'))
def searchIndex():
    if request.method == 'POST':
        # Code to handle form response
        pass      

    return render_template('search.html')