#def row_maximums(my_multidimensional_list):
#	out_dict = {}
#	for rowindex in range(0, len(my_multidimensional_list)):
#		max = 0
#		for item in my_multidimensional_list[rowindex]:
#			if item > max:
#				max = item
#		name = "row",rowindex,'max'
#		name = str(name).replace(",",'').replace("""('""",'').replace("""' """,' ').replace(""" '"""," ").replace("""')""","")
#		out_dict[name] = max
#	return out_dict



def row_maximums(my_multidimensional_list):
    def calculate_my_max(some_list):
        sample_max = some_list[0]
        for number in some_list:
            if number >= sample_max:
                sample_max = number

        return sample_max

    list_of_max = []
    for rows in my_multidimensional_list:
        my_max = calculate_my_max(rows)
        list_of_max.append(my_max)
    #my_sorted_list = sorted(list_of_max)
    my_dict = {}
    for x in range(0, len(list_of_max)):
        my_string = 'row' + " " +  str(x) + " " + 'max'
        my_dict[my_string] = list_of_max[x]
    
    return my_dict



test = [[5, 0, 0, 0, 13], [0, 12, 0, 0], [20, 0, 11, 0], [6, 0, 0, 8]]
print (row_maximums(test))