from flask import (
    Flask,Blueprint,render_template
)

bp = Blueprint('upload_data2excel', __name__)

@bp.route('/upload_data2excel/')
def upload_data2excelt():
    return render_template('upload_data2excelt.html')