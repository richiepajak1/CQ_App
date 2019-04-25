#dummy
#Creates a dictionary(data_dict) of dictionaries(new_dict) containing all of the possible actions a user can take
#Creates a dictionary(student_dict) that stores the student's atributes
import xlrd

loc = 'testfile.xlsx'

wb = xlrd.open_workbook(loc)
print wb.sheet_names()
sheet1 = wb.sheet_by_name('Sheet1')
sheet2 = wb.sheet_by_name('Sheet2')

student_dict = {
    "name": sheet1.cell_value(1, 0),
    "total_score": sheet1.cell_value(1, 1),
    "drive_score": sheet1.cell_value(1, 2),
    "knowledge_score": sheet1.cell_value(1, 3),
    "strategy_score": sheet1.cell_value(1, 4),
    "action_score": sheet1.cell_value(1, 5)
}

data_dict = {}

i = 1
for x in range(1, sheet2.nrows):
    new_dict = {
        "action": sheet2.cell_value(i, 0),
        "category": sheet2.cell_value(i, 1),
        "maximum": sheet2.cell_value(i, 2)
    }
    data_dict[i - 1] = new_dict
    i += 1


