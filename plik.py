import openpyxl as op
from pomoc import obrobka
from sql import result_tab

def generacja_pliku(nazwa = None, *args, **kwargs):
    wb = op.Workbook()

    wb.save(filename=nazwa)

def arkusze(writer, df):
    for x in result_tab:
        x = str(x)
        x = obrobka(x = x)
        x = x.strip()
        temp_df = df[df.Color == str(x)]
        temp_df.to_excel(writer, sheet_name=str(x))
    df.to_excel(writer, sheet_name='all table')