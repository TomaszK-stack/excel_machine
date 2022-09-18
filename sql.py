import pyodbc as py
# from sqlalchemy

def data_base_access(query_1, *args):

    conn_str = ("Driver={SQL Server};"
                "Server=DESKTOP-G5UAGDV\SQLEXPRESS;"
                "Database=AdventureWorks2019;"
                "Trusted_Connection=yes;")
    conn = py.connect(conn_str)

    cursor = conn.cursor()

    query_1 = cursor.execute(query_1)

    return query_1


id_data_od = str(200801)
id_data_do = str(200812)

kwera = 'select distinct Color from Production.Product where id_data between ' + id_data_od +' and ' + id_data_do + 'and color is not null'
kwera_2 = 'select count(*) from Production.Product'

result = data_base_access(query_1=kwera)
liczba_przypadkow = data_base_access(query_1=kwera_2)

liczba_przypadkow_temp  = []

for x in liczba_przypadkow:
    liczba_przypadkow_temp.append(str(x))


result_tab = []
for x in result:
    result_tab.append(x)

dest_table = 'Product'

for x in data_base_access(kwera):
    print(x)


