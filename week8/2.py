def construct_dictionary_from_file_sample2_(filename):
    my_dictionary = {}
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open(filename, mode)
    data = file_pointer.readlines()
    for line in data:
        # Skip any lines that start with #
        if line[0] != '#':
            # Split the line with the delimiter comma (',')
            name, math, physics, chemistry, biology = line.strip().split(',')
            if float(math) > 70 and float(chemistry) > 70:
                my_dictionary[name] = [float(math), float(physics), float(chemistry), float(biology)]
    return my_dictionary