def _list_manipulation_sample5_(my_list):
    input_list = my_list[:]
    for x in range(0, len(input_list)):
        if input_list[x] % 2 != 0:
            input_list[x] = input_list[x] + 1
    return input_list