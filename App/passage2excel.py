from flask import (
    Blueprint, flash, render_template, redirect, url_for, request
)

from . import upload

import xlsxwriter

bp = Blueprint('passage2excel', __name__)

wb = xlsxwriter.Workbook('passage2excel.xlsx')
ws = wb.add_worksheet()

class UplodeSheet:

  def __init__(self, row, col, data):
    self.row = row
    self.col = col
    self.col = data

  def upload_col(row, col, data):
    for i in range(len(data)):
      ws.write(row, col, data[i])
      col += 1

  def upload_row(row, col, data):
    for i in range(len(data)):
      print(f"{row} , {col}, {data[i]}")
      ws.write(row, col, data[i])
      col += 1


@bp.route('/passage2excel/', methods=['GET', 'POST'])
def passage2excel():
    if request.method == 'POST':
        if 'dataform' in request.form:
            row = request.form['nofrow']
            col = request.form['nofcol']
            nsep = request.form['nofsep']
            print(row,col,nsep)
            data = request.form['data']
            print(data)
            write(row,col,nsep,data)
            wb.close()
            return redirect(url_for('passage2excel'))
    
    return render_template('upload_passage_data.html')


def write(row, col, nsep, data):
    pass