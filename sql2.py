from sqlalchemy import create_engine
import pandas as pd


Server = 'DESKTOP-G5UAGDV\SQLEXPRESS'
Database = 'AdventureWorks2019'
Driver = 'ODBC Driver 17 for SQL Server'

Database_con = 'mssql+pyodbc://' + Server + '/' + Database + '?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server'
engine = create_engine(Database_con)
con = engine.connect()
df = pd.read_sql_query( 'Select * from Production.Product' , con = con)


if __name__ == "__main__":
    print(df)
