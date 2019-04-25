#dummy
#Creates a dictionary(datadict) of dictionaries(newdict) containing all of the possible actions a user can take
import xlrd

loc = 'testfile.xlsx'

wb = xlrd.open_workbook(loc)
print wb.sheet_names()
sheet = wb.sheet_by_name('Sheet2')

datadict = {}

i = 1
for x in range(1, sheet.nrows):
    newdict = {
        "action": sheet.cell_value(i, 0),
        "category": sheet.cell_value(i, 1),
        "maximum": sheet.cell_value(i, 2)
    }
    datadict[i-1] = newdict
    i += 1

print datadict[0]
