def maximum_even_value_sample_(sample_2d_list):
    def max_even_of_1d_list(input_list):
        result=None
        for element in input_list:
            if element%2 ==0: # if element is even
                if result==None or element>result:
                    result=element
        return result
    if not sample_2d_list: # list is empty
        return None
    result=None
    for row in sample_2d_list:
        row_max=max_even_of_1d_list(row)
        if row_max:
            if result==None or row_max>result:
                result=row_max
    return result