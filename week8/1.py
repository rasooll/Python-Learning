def construct_dictionary_from_file_sample_(filename):
    my_dictionary = {}
    # Make a connection to the file
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()
    for line in data:
        name, course1, course2, course3, course4 = line.strip().split(',')
        my_dictionary[name] = [float(course1), float(course2), float(course3), float(course4)]
    return my_dictionary
