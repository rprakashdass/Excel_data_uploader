import openpyxl, xlsxwriter

wb = xlsxwriter.Workbook('Guys.xlsx')
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

def process_info(pas):

    slst = pas.split('\n')
    infod = {}

    for i in range(3):
        if not None:
            key, value = map(str, slst[i].split(':'))
            infod[key.strip()] = value.strip()

    return infod


row, col = 0, 0

info_list = []
row_data = []

col_data = [
    "Name",
    "Mobile No",
    "Email",
]

input_list = []

strength = len(input_list)
up_obj = UplodeSheet

def read_data():
  nofdata = int(input("Enter the Number of Inputs"))
  input_list = [input() for i in range(nofdata)]

up_obj.upload_col(0, 0, col_data)

for i in range(strength):
    info_list.append(process_info(input_list[i]))

for i in range(strength):
    row_data = []
    dict_col = info_list[i]
    print(i+1)
    for value in dict_col:
      row_data.append(dict_col[value])
    row += 1
    up_obj.upload_row(row, col, row_data)


wb.close()