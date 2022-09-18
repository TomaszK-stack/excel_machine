import win32com.client as win32


excel = win32.Dispatch('Excel.Application')
excel.Visible = True
workbook = excel.Workbooks.Add()
workbook.SaveAs('D:\\excel_machine\\nowy.xls')
