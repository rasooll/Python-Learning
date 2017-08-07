def _average_of_a_2d_list_sample_(sample_2d_list):
    # Initialize total sum to be 0
    total_sum = 0
    number_of_items=0
    # Get the length of rows and columns
    for row_index in range(len(sample_2d_list)):
        for col_index in range(len(sample_2d_list[row_index])):
            total_sum=total_sum+sample_2d_list[row_index][col_index]
            number_of_items=number_of_items+1
    return total_sum/number_of_items