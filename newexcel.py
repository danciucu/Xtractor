import os
import openpyxl

import globalvars


class field_notes():
    def __init__(self) -> None:
        pass

    def create(dictionary):
        excel_path = 'C:/Users/' + globalvars.user_path + '/AECOM/KYTC NBIS Inspections - 2024-01/400_Technical/200_Templates/MACRO_Inspection Element Library_SNBI.xlsm'
        excel_template = r'%s' % excel_path
        # create a new excel file
        wb = openpyxl.load_workbook(excel_template)
        sheet = wb['Info, NBI, Work']
        # sheet to copy
        sheet_to_copy = wb['# - Element Temp'] 
        # populate the cells
        for keyword in dictionary:
            if keyword == 'Elements':
                for j in range(len(dictionary[keyword][1])):
                    # add the notes into the first tab
                    cell_obj0 = sheet.cell(row = dictionary['Elements'][0][j][0], column = dictionary['Elements'][0][j][1], value = dictionary['Elements'][1][j])
                    cell_obj1 = sheet.cell(row = dictionary['Total Quantity'][0][j][0], column = dictionary['Total Quantity'][0][j][1], value = dictionary['Total Quantity'][1][j])
                    cell_obj2 = sheet.cell(row = dictionary['CS1'][0][j][0], column = dictionary['CS1'][0][j][1], value = dictionary['CS1'][1][j])
                    cell_obj3 = sheet.cell(row = dictionary['CS2'][0][j][0], column = dictionary['CS2'][0][j][1], value = dictionary['CS2'][1][j])
                    cell_obj4 = sheet.cell(row = dictionary['CS3'][0][j][0], column = dictionary['CS3'][0][j][1], value = dictionary['CS3'][1][j])
                    cell_obj5 = sheet.cell(row = dictionary['CS4'][0][j][0], column = dictionary['CS4'][0][j][1], value = dictionary['CS4'][1][j])
                    cell_obj6 = sheet.cell(row = dictionary['Description'][0][j][0], column = dictionary['Description'][0][j][1], value = dictionary['Description'][1][j])  
                    # create new tabs with the elements number
                    new_sheet = wb.copy_worksheet(sheet_to_copy)
                    new_sheet.title = dictionary['Elements'][1][j]
                    wb.move_sheet(new_sheet, offset = -2)
                    # add to the tab the informations
                    cell_obh0 = new_sheet.cell(row = 2, column = 1, value = dictionary['Elements'][1][j])
                    cell_obh1 = new_sheet.cell(row = 4, column = 4, value = dictionary['Total Quantity'][1][j])
                    cell_obh2 = new_sheet.cell(row = 4, column = 6, value = dictionary['CS1'][1][j])
                    cell_obh3 = new_sheet.cell(row = 4, column = 7, value = dictionary['CS2'][1][j])
                    cell_obh4 = new_sheet.cell(row = 4, column = 8, value = dictionary['CS3'][1][j])
                    cell_obh5 = new_sheet.cell(row = 4, column = 9, value = dictionary['CS4'][1][j])
                    cell_obh6 = new_sheet.cell(row = 17, column = 1, value = dictionary['Description'][1][j])
                break
            else:   
                cell_obj_main = sheet.cell(row = dictionary[keyword][0][0], column = dictionary[keyword][0][1], value = dictionary[keyword][1])
        # save the file
        wb.save(os.path.join(globalvars.save_path, dictionary['Structure ID'][1] + ' Field Notes '+ globalvars.inspection_date[0:4] + globalvars.inspection_date[5:7] +'DD.xlsx'))
        wb.close()  