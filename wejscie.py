try:
    import pyodbc
except ImportError:
    import odbc as pyodbc
import pandas as pd
import pandas.io.sql as sql
import warnings
# id_data_od = input('data od: ')
# id_data_do = input('data do: ')

id_data_od = str(200801)
id_data_do = str(200812)


conn_str = ("Driver={SQL Server};"
            "Server=DESKTOP-G5UAGDV\SQLEXPRESS;"
            "Database=AdventureWorks2019;"
            "Trusted_Connection=yes;")
conn = pyodbc.connect(conn_str)

sql_query = sql.read_sql_query('select * from Production.Product where id_data between '+id_data_od + 'and ' + id_data_do   ,conn )

df = pd.DataFrame(sql_query)
print(df)