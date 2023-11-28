import os
import openpyxl

class field_notes():
    def __init__(self) -> None:
        pass

    def create(excel_template, savepath, filename, elements_str, elements_int, quantities):
        # total number of elements per txt file
        no_elements = len(elements_int)
        # create a new excel file
        wb = openpyxl.load_workbook(excel_template)
        sheet = wb['Info, NBI, Work']
        sheet_to_copy = wb['# - Element Temp']
        # loop over all the elements extracted
        for i in range(no_elements):
            # add the notes into the first tab
            cell_obj0 = sheet.cell(row = 84 + i, column = 1, value = elements_str[i])
            cell_obj1 = sheet.cell(row = 84 + i, column = 2, value = quantities[0][i])
            cell_obj2 = sheet.cell(row = 84 + i, column = 3, value = quantities[1][i])
            cell_obj3 = sheet.cell(row = 84 + i, column = 4, value = quantities[2][i])
            cell_obj4 = sheet.cell(row = 84 + i, column = 5, value = quantities[3][i])
            cell_obj5 = sheet.cell(row = 84 + i, column = 6, value = quantities[4][i])
            cell_obj6 = sheet.cell(row = 84 + i, column = 7, value = quantities[5][i])                
            # create new tabs with the elements number
            new_sheet = wb.copy_worksheet(sheet_to_copy)
            new_sheet.title = elements_str[i]
            wb.move_sheet(new_sheet, offset = -2)
            # add to the tab the informations
            cell_obh0 = new_sheet.cell(row = 2, column = 1, value = elements_int[i])
            cell_obh1 = new_sheet.cell(row = 4, column = 4, value = quantities[0][i])
            cell_obh2 = new_sheet.cell(row = 4, column = 6, value = quantities[1][i])
            cell_obh3 = new_sheet.cell(row = 4, column = 7, value = quantities[2][i])
            cell_obh4 = new_sheet.cell(row = 4, column = 8, value = quantities[3][i])
            cell_obh5 = new_sheet.cell(row = 4, column = 9, value = quantities[4][i])
            cell_obh6 = new_sheet.cell(row = 17, column = 1, value = quantities[5][i])
        # save the file
        wb.save(os.path.join(savepath, filename + ' Field Notes 2023MM.xlsx'))
        wb.close()     