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

                    if keyword == 'Main Design':
                        value = lines[i + 1].split()

                    else:
                        index = line.index(keyword) + len(keyword)
                        value = line[index:].split()

                    return value

        # Define a list of keywords you want to search for
        keywords = [
            'Structure Num', 
            'Routine', 
            'Route Num (5D):',
            'Kind of Hwy (5B',
            'Posting Status', 
            'SUPERSTRUCTURE CONDITION', 
            'CULVERT CONDITION', 
            'Main Design',
            'Deck Rating',
            'Superstructure Rating',
            'Substructure Rating',
            'Culvert Rating',
            'Scour Observed'
            # Add more keywords here as needed
            ]
        
        # Define a list of cells you want to populate
        cells = [
            # row, column
            [1,    2],
            [5,    3],
            [7,    2],
            [7,    2],
            [9,    5],
            [14,    2],
            [14,    2],
            [16,    2],
            [25,    2],
            [28,    2],
            [31,    2],
            [34,    2],
            [20,    5]
            # Add more cells here as needed
            ]
        
        # Route Signing Prefix
        route = {'1': 'I', '2': 'US', '3': 'KY', '4': 'CR', '5': 'CS'}

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
                #value = 'No Scour'

            # populate the data dictionary
            try:
                if keyword == 'Kind of Hwy (5B':
                    data[keyword] = route[value[0]]
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