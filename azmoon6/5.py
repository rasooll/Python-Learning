def calculate_expenses(filename):

    my_dictionary = {}
    # Make a connection to the file
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()
    
    for line in data:
        line = line.strip().split(',')
        my_item = line[0].strip()
        my_price = float(line[1].strip())
      
        if my_item not in my_dictionary:
            my_dictionary[my_item] =  my_price
        else:
            my_dictionary[my_item] +=  my_price
    my_list = []
    my_keys = sorted(my_dictionary.keys())
    for x in my_keys:
        my_list.append((x,"${0:.2f}".format(my_dictionary[x])))
    return my_list