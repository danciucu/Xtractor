import os
import tkinter, ttkthemes, tkinter.filedialog

import globalvars, file_import, inspection_reports, inspection_elements, newexcel

class Xtractor(ttkthemes.ThemedTk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('XtractoR')
        self.geometry('300x300')
        self.set_theme('radiance')
        # define a frame
        self.main_frame = tkinter.ttk.Frame(self)
        self.main_frame.pack()
        ## label for directory path
        self.dirpath_label = tkinter.ttk.Label(self.main_frame, text = 'Directory Path')
        self.dirpath_label.grid(row = 0, column = 1)
        ## entry for directory path
        self.dirpath_entry = tkinter.ttk.Entry(self.main_frame, width = 30, state = tkinter.NORMAL)
        self.dirpath_entry.grid(row = 1, column = 1)
        ## button for directory path
        self.dirpath_button = tkinter.ttk.Button(self.main_frame, text = '...', state = tkinter.NORMAL, command = self.txt_import, width = 2)
        self.dirpath_button.grid(row = 1, column = 2)
        ## label for save path
        self.savepath_label = tkinter.ttk.Label(self.main_frame, text = 'Save Path')
        self.savepath_label.grid(row = 2, column = 1)
        ## entry for save path
        self.savepath_entry = tkinter.ttk.Entry(self.main_frame, width = 30, state = tkinter.NORMAL)
        self.savepath_entry.grid(row = 3, column = 1)
        ## button for save path
        self.savepath_button = tkinter.ttk.Button(self.main_frame, text = '...', state = tkinter.NORMAL, command = self.save_path, width = 2)
        self.savepath_button.grid(row = 3, column = 2) 
        ## button for starting the process
        self.start_button = tkinter.ttk.Button(self.main_frame, text = 'Start', command = self.generate_excel, width = 4)
        self.start_button.grid(row =4, column = 1)

    def txt_import(self):
        # variable that handles the Excel path
        folder_path = tkinter.filedialog.askdirectory()
        # fill entry bar with the path
        self.dirpath_entry.insert(tkinter.END, folder_path)
        # set the path for the txt files
        globalvars.dirpath = folder_path


    def save_path(self):
        # variable that handles the Excel path
        folder_path = tkinter.filedialog.askdirectory()
        # fill entry bar with the path
        self.savepath_entry.insert(tkinter.END, folder_path)
        # set the path for saving files
        globalvars.savepath = folder_path

    # comment
    def generate_excel(self):
        # create empty string variables
        filename = ''
        filepath = ''
        notes = ''
        elements = ''
        qunatities = ''
        excel_template = r''
        # get the number of .txt files are in the folder
        file_numbers = len(os.listdir(globalvars.dirpath))
        # loop over the entire number of txt files available
        for i in range(file_numbers):
            # create filepath
            filepath = file_import.txtfile.import_file(globalvars.dirpath, i)
            # get the filename
            filename = file_import.txtfile.get_filename(globalvars.dirpath, i)
            # get inspection notes
            notes = inspection_reports.notes.comments(filepath)
            # get elements' number
            elements = inspection_elements.properties.element_number(notes)
            # get quantities
            qunatities = inspection_elements.properties.element_quantities(notes)
            # create a new excel spreadsheet
            newexcel.field_notes.create(excel_template, globalvars.savepath, filename, elements, qunatities)

            
if __name__ == "__main__":
    app = Xtractor()
    app.mainloop()
