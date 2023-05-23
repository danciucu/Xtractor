class notes():
    def __init__(self) -> None:
        pass

    def comments(filepath):
        # create an empty array
        elements = []
        # open the txt file
        file = open(filepath, 'r')
        # read the lines of the file
        lines = file.readlines()
        # create a variable that loops over the lines
        lineofinterest = 0
        # create a variable to monitor the empty lines
        breaklines = 0
        # create a variable to loop over the lines of interest
        i = 0

        # define a loop that goes over all the lines in the txt file
        while True:
            # update variable
            lineofinterest += 1
            # if the line contains what the user is looking for
            if ('ELEM   ELEMENT NAME' in lines[lineofinterest]) or ('814 AC Wearing' in lines[lineofinterest + 1]) or ('515 Steel' in lines[lineofinterest + 1]):
                # loop over the lines below the line that contains the wanted string
                while i < len(lines) - lineofinterest:
                    # update variable
                    i += 1
                    # if the line is empty
                    if len(lines[lineofinterest + i]) < 2:
                        # update variable
                        breaklines += 1
                        # if there were two empty lines from the beginning
                        if breaklines == 2:
                            # update variables and stop
                            breaklines = 0
                            i = 0
                            break
                    # if the line contains 'Inspection' jump 8 lines
                    if 'Inspection' in lines[lineofinterest + i]:
                        i += 7
                        continue
                    # if the previous line contains the child element, skip the current line because it has only one word (i.e. Surface or Protective)
                    if (('Surface' in lines[lineofinterest + i]) and ('814 AC Wearing' in lines[lineofinterest + i - 1])) or (('Protective' in lines[lineofinterest + i]) and ('515 Steel' in lines[lineofinterest + i - 1])):
                        continue
                    # if the line is not empty add it to the elements array
                    if len(lines[lineofinterest + i]) > 2:
                        elements.append(lines[lineofinterest + i])
            #if '813 AC Wearing' or '515 Steel' in lines[lineofinterest]:

            # if the line contains 'Work Candidates Report' then stop the process
            if 'Work Candidates Report' in lines[lineofinterest]:
                # close txt file
                file.close()
                return elements