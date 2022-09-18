# from sql import liczba_przypadkow_temp
from sql2 import df, engine
from sqlalchemy import Column, String
import pandas as pd
# zmienna = liczba_przypadkow_temp[0]


def obrobka(x):
    if str(x) != x:
        raise ValueError
    else:
        x = x.replace("'", "").replace(',', '').replace(')', '').replace('(', '')
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
if __name__ == "__main__":
    id_data = create_id_data(df)

    for x,y in zip(df.ProductID, id_data.id_data):
        print(x,y)
        engine.execute('update Production.Product set id_data = ' + str(y) + ' where ProductID = ' + str(x))

    # print(create_id_data(df))



    # id_data = create_id_data(df)
    # column = Column('new_column_name', String(100))
    # # column = id_data.to_sql('id_data', engine)
    # print(type(column))
    # add_column(engine, 'Production.Product', column)




array = [1,2,3,4]
array.sort()