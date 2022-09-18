import xlwings as xw
from wejscie import df
from sql import result_tab, liczba_przypadkow_temp
import pandas as pd
from wejscie import df
import win32com.client as win32
import openpyxl
import os
from plik import generacja_pliku, arkusze
from plots import myplot
from pomoc import obrobka


sciezka = 'empty_book.xlsx'
# Stworzenie pustego pliku

generacja_pliku(nazwa=sciezka)

# arkusze
df = df.astype({'Color':'string'})
writer = pd.ExcelWriter(path = sciezka , engine = 'openpyxl')
arkusze(writer=writer, df=df)
writer.save()
a


wb = xw.Book(sciezka)
wb.sheets.add(name='Title page')
title_sheet = wb.sheets[0]

title_sheet.range('A1:Z1').merge()



title_sheet.range('A1').value = 'Podsumowanie:'
title_sheet.range('A2').value = 'Liczba przypadków: ' + str(obrobka(liczba_przypadkow_temp[0]))


# myplot(n = 14, caller=ws)
wb.save('new_empty.xlsx')











