def generate_dict():
    brm_dict = {
        'Structure ID': [[1, 2], ''],
        'Date': [[4, 2], ''],
        'Route #': [[7, 2], ''],
        'Bridge/Culvert': [[14, 2], ''],
        'B.C.01 (Deck) (Item 58)': [[25, 2], ''],
        'B.C.02 (Superstructure) (Item 59)': [[28, 2], ''],
        'B.C.03 (Substructure) (Item 60)': [[31, 2], ''],
        'B.C.04 (Culverts) (Item 62)': [[34, 2], ''],
        'B.C.09 (Channel) (Item 61)': [[49, 2], ''],
        'B.AP.02 (Overtopping Likelihood) (Item 71 - Waterway Adequacy)': [[55, 2], ''],
        'Scour Observed': [[20, 5], ''],
        # max is 70 for work items
        #'Work Items': [[[60, 1]], ['']],
        'Elements': [[], []],
        'Total Quantity': [[], []],
        'CS1': [[], []],
        'CS2': [[], []],
        'CS3': [[], []],
        'CS4': [[], []],
        'Description': [[], []]
    }

    return brm_dict