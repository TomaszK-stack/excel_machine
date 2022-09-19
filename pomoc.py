# from sql import liczba_przypadkow_temp
from sql2 import df, engine
from sqlalchemy import Column, String
import pandas as pd
import xlwings as xw

def obrobka(x):
    if str(x) != x:
        raise ValueError
    else:
        x = x.replace("'", "").replace(',', '').replace(')', '').replace('(', '').strip()
    return x
# if __name__ == "__main__":
#     print(obrobka(zmienna))
#


def create_id_data(data):
    temp_id_data = []
    temp_table_id = []
    id_data = None
    for x, y in zip(data.SellStartDate, data.ProductID):
        x = str(x).split(sep = ' ')[0]
        id_data = x.split(sep = '-')[0] + x.split(sep = '-')[1]
        temp_id_data.append(id_data)
        temp_table_id.append(y)


    temp_id_data = pd.DataFrame(data = {'id_data' : temp_id_data, 'ProductID': temp_table_id})
    return temp_id_data

def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD %s %s' % (table_name, column_name, column_type))

def dodanie_fitra(tab_z_arkuszami, caller):
    sheet = None
    for x in tab_z_arkuszami:
        x = obrobka(str(x))
        print(x)
        sheet = caller.sheets[x]
        sheet.used_range.api.AutoFilter(Field:=1)

def kolorowanie_kolumn(caller, arkusz):
    sheet = caller.sheets[arkusz]
    sheet.range("B3").api.Font.ColorIndex = 4


def podsumowanie(caller, tab_z_ark):
    tab_z_ark.append('all table')
    for x in tab_z_ark:
        x = obrobka(str(x))
        sheet = caller.sheets[x]
        l_r = int(lastRow(idx=x, workbook=caller)) + 4
        rng = 'A' + str(l_r)
        sheet[rng].value = 'Podsumowanie'
        sheet.range(rng).api.Font.Size = 20





def lastRow(idx, workbook, col=1):
    """ Find the last row in the worksheet that contains data.

    idx: Specifies the worksheet to select. Starts counting from zero.

    workbook: Specifies the workbook

    col: The column in which to look for the last cell containing data.
    """

    ws = workbook.sheets[idx]

    lwr_r_cell = ws.cells.last_cell      # lower right cell
    lwr_row = lwr_r_cell.row             # row of the lower right cell
    lwr_cell = ws.range((lwr_row, col))  # change to your specified column

    if lwr_cell.value is None:
        lwr_cell = lwr_cell.end('up')    # go up untill you hit a non-empty cell

    return lwr_cell.row















if __name__ == "__main__":
    id_data = create_id_data(df)

    for x,y in zip(df.ProductID, id_data.id_data):
        print(x,y)
        engine.execute('update Production.Product set id_data = ' + str(y) + ' where ProductID = ' + str(x))

    print(create_id_data(df))
    id_data = create_id_data(df)
    column = Column('new_column_name', String(100))
    # column = id_data.to_sql('id_data', engine)
    print(type(column))
    add_column(engine, 'Production.Product', column)




