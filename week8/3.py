def construct_nested_list_from_file_sample_(filename):
    my_dictionary = {}
    my_dictionary["milk"] = []
    my_dictionary["bread"] = []
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open(filename, mode)
    data = file_pointer.readlines()
    for line in data:
        first_character = line[0]
        if first_character == "m":
            # remove the first character
            # strip and split by white space
            vertex = line[1::].strip().split()
            # change the string items into floats
            vertex = [float(x) for x in vertex]
            my_dictionary["milk"] += [vertex]

        if first_character == "b":
            face = line[1::].strip().split()
            face = [float(x) for x in face]
            my_dictionary["bread"] += [face]
    return my_dictionary