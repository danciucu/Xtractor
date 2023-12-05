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
            'Location', 
            'Posting Status', 
            'SUPERSTRUCTURE CONDITION', 
            'CULVERT CONDITION', 
            'Main Design'
            # Add more keywords here as needed
            ]
        
        # Define a list of cells you want to populate
        cells = [
            # row, column
            [1,    2],
            [4,    3],
            [7,    2],
            [9,    5],
            [14,    2],
            [14,    2],
            [16,    2]
            # Add more cells here as needed
            ]

        # Create a dictionary to store the extracted values
        data = {}
        # Create a dictionary to store the locations
        location = {}
        for i, keyword in enumerate(keywords):
            # get the value 
            value = extract_value(keyword)
            
            if keyword == 'SUPERSTRUCTURE CONDITION' and not value:
                value = ['Bridge']
            elif keyword == 'CULVERT CONDITION' and not value:
                 value == ['Culvert']
            elif keyword == 'Posting Status':
                if value[2] == 'Posted':
                    value = ['Yes']
                else:
                    alue = ['No']
            # populate the data dictionary
            try:
                data[keyword] = value[0]
            except:
                data[keyword] = value
            # populate the location dictionary
            location[keyword] = cells[i]
        # Print the organized data
        #for key, value in data.items():
        #    print(f"{key}: {value}")
        #print(location)

        return [keywords, data, location]