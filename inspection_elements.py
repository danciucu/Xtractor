class properties():
    def __init__(self) -> None:
        pass

    # function that extracts the inspection notes
    def element_number(notes):
        # create empty variables
        digits = 0
        first_digit = 0
        last_digit = 0
        # create empty array
        elements = []
    
        # loop over all the sentences/strings in the notes
        for strings in notes:
            # loop over the charactes of each string
            for i in range(len(strings)):
                # if the character is a digit and the number of digits is null
                if strings[i].isdigit() == True and digits == 0:
                    # update first_digit and the digits count
                    first_digit = i
                    digits += 1
                # if the character is a digit and the next character is not
                if strings[i].isdigit() == True and strings[i + 1].isdigit() == False:
                    # update last_digit and then stop
                    last_digit = i
                    break
            # if the lenght of the string from first_digit to last_digit + 1 is greater than 1 and the first_digit is within the first 10 chars and "/20" string is inside of strings
            if len(strings[first_digit:last_digit + 1]) > 1 and len(strings) > 35 and first_digit < 6 and "/20" in strings:
                # update the elements array
                elements.append(strings[first_digit:last_digit + 1])

            # reset varables
            digits = 0
            first_digit = 0
            last_digit = 0

        return elements

    # function that extracts the element quantities and the description
    def element_quantities(notes):
        # create empty variables
        slashes = 0
        last_slash = 0
        count = 0
        # create empty arrays
        strings_main = []
        quantities = []
        total_qunatities = []
        cs1_quantities = []
        cs2_quantities = []
        cs3_quantities = []
        cs4_quantities = []
        description = []
        strings_description = []
        # create an empty string
        temp = ''

        # loop over the strings in the notes
        for strings in notes:
            # update count
            count += 1
            # if there is a slash followed by two digits inside of the string
            if '.00' in strings[len(strings) - 6 : len(strings) - 1]:
                # remember the key of that string
                strings_main.append(count)
                # loop over the characters in that string
                for i in range(len(strings)):
                    # if there is a slash followed by a number
                    if strings[i] == "/" and strings[i + 1].isdigit() == True:
                        # update slashes variable
                        slashes += 1
                        # if there are two slahses found
                        if slashes == 2:
                        # remember the location of last slash and stop
                            last_slash = i
                            break
                # add the string.split() from last_slash to quantities array 
                quantities.append(strings[last_slash:].split())
            # if there ar no slashes
            else:
                # remember the key of that string
                strings_description.append(count)

        # add the last key where the last string is ending
        strings_main.append(len(notes) + 1)
        
        # reset variables
        slashes = 0
        last_slash = 0

        count = 0

        # loop over splitted values of the quantities
        for quantity in quantities:
            # update total quantities
            total_qunatities.append(quantity[1])
            # check the lenght of the array of strings
            try:
                cs1_quantities.append(quantity[len(quantity) - 4])
            except:
                cs1_quantities.append('?')
            try:
                cs2_quantities.append(quantity[len(quantity) - 3])
            except:
                cs2_quantities.append('?')
            try:
                cs3_quantities.append(quantity[len(quantity) - 2])
            except:
                cs4_quantities.append('?')
            try:
                cs4_quantities.append(quantity[len(quantity) - 1])
            except:
                cs4_quantities.append('?')

        # loop over all stings are not comments
        for i in range(len(strings_main)):
            if i == len(strings_main) - 1:
                difference = 1
            else:
                difference = int(strings_main[i + 1] - strings_main[i])
            for j in range(1, difference):
                temp += notes[int(strings_main[i] + j - 1)]

            description.append(temp.replace("\n", ''))
            temp = ''

        return [total_qunatities, cs1_quantities, cs2_quantities, cs3_quantities, cs4_quantities, description]