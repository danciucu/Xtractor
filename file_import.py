import os

class txtfile():
    def __init__(self) -> None:
        pass

    # function that returns the path of the txt file
    def import_file(directory, index):
        # get the folder's path
        file = os.listdir(directory)
        # join the folder's path with the name of the file
        path = os.path.join(directory, file[index])
        return path 
    
    # function that returns the bridge ID
    def get_filename(directory, index):
        # get the folder's path
        file = os.listdir(directory)
        # get the file name
        filename = file[index][len(file[index]) - 25:len(file[index]) - 15]  
        return filename
