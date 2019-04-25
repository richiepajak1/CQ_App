#dummy

import xlrd
import xlwt
import json


def pull_from_excel(filename):
    """
    pulls data from excel file
    this should only be used the first time the app is run

    :param filename: name of excel file
    :return: a list containing two dictionaries: the first is the student info, the second is a dictionary
        of dictionaries containing the info about the actions
    """

    wb = xlrd.open_workbook(filename)
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

    action_dict = {}

    i = 1
    for x in range(1, sheet2.nrows):
        new_dict = {
            'action': sheet2.cell_value(i, 0),
            'category': sheet2.cell_value(i, 1),
            'points': sheet2.cell_value(i, 2),
            'maximum': sheet2.cell_value(i, 3),
            'times_completed': sheet2.cell_value(i, 4)
        }
        action_dict[i - 1] = new_dict
        i += 1

    dict_list = [student_dict, action_dict]
    return dict_list


def push_to_json(dict, filename):
    """
    stores dictionary in json file
    :param dict: dictionary to be stored
    :param filename: name of the file the dictionary will be stored in
    :return: none
    """

    with open(filename, 'w') as json_file:
        json.dump(dict, json_file)



def pull_from_json(filename):
    """
    pulls data from json file
    :param filename: name of the filename to be pulled from
    :return: dictionary containing the data
    """
    with open(filename) as f:
        data = json.load(f)
    return data


def push_to_excel(student_dict, action_dict):
    """
    todo write documentation
    :param student_dict:
    :param action_dict:
    :return:
    """
    filename = 'python_excel_test.xls'
    excel_file = xlwt.Workbook()
    sheet1 = excel_file.add_sheet('Sheet1')
    sheet1.write(0, 0, 'Name')
    sheet1.write(0, 1, 'TotalScore')
    sheet1.write(0, 2, 'DriveScore')
    sheet1.write(0, 3, 'KnowledgeScore')
    sheet1.write(0, 4, 'StrategyScore')
    sheet1.write(0, 5, 'ActionScore')
    sheet1.write(1, 0, student_dict['name'])
    sheet1.write(1, 1, student_dict['total_score'])
    sheet1.write(1, 2, student_dict['drive_score'])
    sheet1.write(1, 3, student_dict['knowledge_score'])
    sheet1.write(1, 4, student_dict['strategy_score'])
    sheet1.write(1, 5, student_dict['action_score'])

    sheet2 = excel_file.add_sheet('Sheet2')
    sheet2.write(0, 0, 'Action')
    sheet2.write(0, 1, 'Category')
    sheet2.write(0, 2, 'Points')
    sheet2.write(0, 3, 'Maximum')
    sheet2.write(0, 4, 'TimesCompleted')
    i = 1
    for x in action_dict:
        sheet2.write(i, 0, action_dict[x]['action'])
        sheet2.write(i, 1, action_dict[x]['category'])
        sheet2.write(i, 2, action_dict[x]['points'])
        sheet2.write(i, 3, action_dict[x]['maximum'])
        sheet2.write(i, 4, action_dict[x]['times_completed'])
        i += 1
    excel_file.save(filename)


def update_action_list(filename, action_dict):
    """
    todo write documentation
    :param filename:
    :param action_dict:
    :return:
    """
    wb = xlrd.open_workbook(filename)
    sheet1 = wb.sheet_by_name('Sheet1')
    i = 1
    for x in range(1, sheet1.nrows):
        currentlen = len(action_dict)
        new_dict = {
            'action': sheet1.cell_value(i, 0),
            'category': sheet1.cell_value(i, 1),
            'points': sheet1.cell_value(i, 2),
            'maximum': sheet1.cell_value(i, 3),
            'times_completed': sheet1.cell_value(i, 4)
        }
        i += 1
        action_dict[currentlen] = new_dict
    return action_dict

