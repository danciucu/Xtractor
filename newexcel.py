import os
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation
from pycel import ExcelCompiler

import globalvars


class field_notes():
    def __init__(self) -> None:
        pass


    def create(dictionary):
        # array for keywords that the loop will skip
        skip_keywords = ['Total Quantity', 'CS1', 'CS2', 'CS3', 'CS4', 'Description', 'Work Items Action', 'Work Items Priority', 'Work Items Responsibility']

        try:
            excel_path = 'C:/Users/' + globalvars.user_path + '/AECOM\KYTC NBIS Inspections - 2023-2025/400_Technical/200_Templates/MACRO_Inspection Element Library_SNBI.xlsx'
            excel_template = r'%s' % excel_path
            # create a new excel file
            wb = openpyxl.load_workbook(excel_template)
            sheet = wb['Info, NBI, Work']
            # sheet to copy
            sheet_to_copy = wb['# - Element Temp'] 
            # populate the cells
            for keyword in dictionary:

                if keyword == 'Work Items Description':
                    for k in range(len(dictionary[keyword][1])):
                        # add working items into the first tab
                        cell_obj0_wi = sheet.cell(row = dictionary['Work Items Description'][0][k][0], column = dictionary['Work Items Description'][0][k][1], value = dictionary['Work Items Description'][1][k])
                        cell_obj1_wi = sheet.cell(row = dictionary['Work Items Action'][0][k][0], column = dictionary['Work Items Action'][0][k][1], value = dictionary['Work Items Action'][1][k])
                        cell_obj2_wi = sheet.cell(row = dictionary['Work Items Priority'][0][k][0], column = dictionary['Work Items Priority'][0][k][1], value = dictionary['Work Items Priority'][1][k])
                        cell_obj3_wi = sheet.cell(row = dictionary['Work Items Responsibility'][0][k][0], column = dictionary['Work Items Responsibility'][0][k][1], value = dictionary['Work Items Responsibility'][1][k])
        
                elif keyword == 'Elements':
                    for j in range(len(dictionary[keyword][1])):
                        # add the notes into the first tab
                        cell_obj0 = sheet.cell(row = dictionary['Elements'][0][j][0], column = dictionary['Elements'][0][j][1], value = int(dictionary['Elements'][1][j]))
                        cell_obj1 = sheet.cell(row = dictionary['Total Quantity'][0][j][0], column = dictionary['Total Quantity'][0][j][1], value = float(dictionary['Total Quantity'][1][j]))
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
                        cell_obh0 = new_sheet.cell(row = 2, column = 1, value = int(dictionary['Elements'][1][j]))
                        cell_obh1 = new_sheet.cell(row = 4, column = 4, value = float(dictionary['Total Quantity'][1][j]))
                        cell_obh2 = new_sheet.cell(row = 5, column = 4, value = float(dictionary['Total Quantity'][1][j]))
                        cell_obh3 = new_sheet.cell(row = 4, column = 6, value = dictionary['CS1'][1][j])
                        cell_obh4 = new_sheet.cell(row = 4, column = 7, value = dictionary['CS2'][1][j])
                        cell_obh5 = new_sheet.cell(row = 4, column = 8, value = dictionary['CS3'][1][j])
                        cell_obh6 = new_sheet.cell(row = 4, column = 9, value = dictionary['CS4'][1][j])
                        cell_obh7 = new_sheet.cell(row = 17, column = 1, value = dictionary['Description'][1][j])
                        # create condition data validation
                        dv1 = DataValidation(type = 'list', formula1 = '"CS1, CS2, CS3, CS4"')
                        new_sheet.add_data_validation(dv1)
                        dv1.add('D19:D61')

                elif keyword in skip_keywords:
                    continue

                else:
                    cell_obj_main = sheet.cell(row = dictionary[keyword][0][0], column = dictionary[keyword][0][1], value = dictionary[keyword][1])
            
            # save the file
            path = os.path.join(globalvars.save_path, dictionary['Structure ID'][1] + ' Field Notes '+ globalvars.inspection_date[0:4] + globalvars.inspection_date[5:7] +'DD.xlsx')
            wb.save(path)

            # get the saved file
            excel = ExcelCompiler(filename=path)
            for i in range(len(dictionary['Elements'][1])):
                # get the element tab
                sheet = dictionary['Elements'][1][i]
                # set it as active sheet
                ws = wb[sheet]
                # get all the defects in C6:C15 cells
                defects = ','.join([str(excel.evaluate(f'{sheet}!C{i}')) for i in range(6, 15)])
                # create defects data validation
                dv2 = DataValidation(type='list', formula1=f'"{defects}"')
                ws.add_data_validation(dv2)
                dv2.add('C19:C61')

            # save the file again
            wb.save(path)

        except Exception as e:
            print("An error occurred:", e)
        finally:
            # close the workbook
            if 'wb' in locals():
                wb.close()