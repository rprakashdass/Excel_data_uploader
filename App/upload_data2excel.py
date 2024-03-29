from flask import (
    Flask,Blueprint,render_template,request
)

from App import upload

bp = Blueprint('upload_data2excel', __name__)

@bp.route('/upload_data2excel/', methods=['GET','POST'])
def upload_data2excelt():
    return render_template('upload_data2excelt.html')

# @bp.route('/sendData')
# def sendData():
#     if request.method == 'POST':
#         nofdata = request.nofdata
#         data = request.data
#     return 