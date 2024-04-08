from flask import (
    Flask,Blueprint,render_template,request, redirect, url_for, flash
)

import xlsxwriter

bp = Blueprint('upload_data2excel', __name__)

@bp.route('/upload_data2excel/', methods=['GET','POST'])
def upload_data2excel():
        return render_template('upload_data2excel_test.html')

@bp.route('/after_upload/', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        data = request.form['input_data']
        print(data)
        wb = xlsxwriter.Workbook('sheet.xlsx')
        ws = wb.add_worksheet()
        ws.write(0,0, data)
        wb.close()
        return redirect(url_for('upload_data2excel'))

    return redirect(url_for('upload_data2excel'))