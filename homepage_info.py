import re

class populate():
    def __init__(self) -> None:
        pass

    def info(filepath):
        # Open the file and read the lines
        with open(filepath, 'r') as file:
            lines = file.readlines()

        # Define a function to extract the value following a keyword
        def extract_value(keyword):
            for i, line in enumerate(lines):
                if keyword in line:

                    index = line.index(keyword) + len(keyword)
                    value = line[index:].split()
                    return value

        # Define a list of keywords you want to search for
        keywords = [
            'Structure Num', 
            'Routine', 
            'Route Num (5D):',
            'Kind of Hwy (5B',
            'ROUTE ON STRUCTURE:',
            'Posting Status', 
            'SUPERSTRUCTURE CONDITION', 
            'CULVERT CONDITION', 
            'Deck Rating',
            'Superstructure Rating',
            'Substructure Rating',
            'Culvert Rating',
            'Scour Observed',
            # Add more keywords here as needed
            ]
        
        # Define a list of cells you want to populate
        cells = [
            # row, column
            [1,    2], # Structure Num
            [5,    3], # Routine
            [7,    2], # Route Num (5D):
            [7,    2], # Kind of Hwy (5B
            [7,    3], # ROUTE ON STRUCTURE
            [9,    5], # Posting Status
            [14,   2], # SUPERSTRUCTURE CONDITION
            [14,   2], # CULVERT CONDITION
            [25,   2], # Deck Rating
            [28,   2], # Superstructure Rating
            [31,   2], # Substructure Rating
            [34,   2], # Culvert Rating
            [20,   5], # Scour Observed
            # Add more cells here as needed
            ]
        
        # Route Signing Prefix
        route = {'1': 'I-', '2': 'US-', '3': 'KY-', '4': 'CR-', '5': 'CS-'}

        # Create a dictionary to store the extracted values
        data = {}
        # Create a dictionary to store the locations
        location = {}
        for i, keyword in enumerate(keywords):
            # get the value 
            value = extract_value(keyword)
            
            # filter the information
            if keyword == 'SUPERSTRUCTURE CONDITION' and not value:
                if value == []:
                    value = ['Bridge']
            elif keyword == 'CULVERT CONDITION' and not value:
                 if value == []:
                    value = ['Culvert']
            elif keyword == 'Posting Status':
                if value[2] == 'Posted':
                    value = ['Yes']
                else:
                    value = ['No']
            elif keyword == 'Deck Rating' or keyword == 'Substructure Rating' or keyword == 'Culvert Rating':
                if value is not None:
                    value = [value[1]]
            elif keyword == 'Scour Observed' and 'No' in value:
                value = ['No Scour']
            elif keyword == 'ROUTE ON STRUCTURE:':
                j = 0
                name = ''
                while value[j] != 'CLASSIFICATION':
                    if len(value[j]) < 2:
                        j += 1
                    name += value[j] + ' '
                    j += 1
                value = name

            # populate the data dictionary
            try:
                if keyword == 'Kind of Hwy (5B':
                    data[keyword] = route[value[0]]
                elif keyword == 'ROUTE ON STRUCTURE:':
                    data[keyword] = value
                else:
                    data[keyword] = value[0]
            except (IndexError, KeyError, TypeError):
                data[keyword] = value

            # populate the location dictionary
            location[keyword] = cells[i]
        # Print the organized data
        #for key, value in data.items():
        #    print(f"{key}: {value}")
        #print(location)

        return [keywords, data, location]
    


    def work_items(filepath):
        initial_corpus = []
        final_corpus = []
        current_lines = []
        # Read the content of the file
        file = open(filepath, 'r')
        # read the lines of the file
        lines = file.readlines()

        for i, line in enumerate(lines):
            if 'Work Candidates Report' in line:
                initial_corpus = lines[i:]


        for line in initial_corpus:
            line_lower = line.lower().strip()

        # Check for the presence of specific keywords
            if 'work candidates report' in line_lower or 'work history' in line_lower:
                continue
            elif any(keyword in line_lower for keyword in ["notes :", "concur", '.']):
                current_lines.append(line.strip())
            elif current_lines:
                final_corpus.append(re.sub('Notes : ', '',(' '.join(current_lines))))
                current_lines = []

        # If there's any remaining content in current_lines, add it to array2
        if current_lines:
            final_corpus.append(re.sub('Notes : ', '',(' '.join(current_lines))))


        return final_corpus