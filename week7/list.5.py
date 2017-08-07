def _sum_of_columns_sample_(sample_list):
    # Solution type 1:
    # return [max(col) for col in zip(*sample_list)]
    # Alternative Solution
    cols = len(sample_list[0])
    mylist = []
    for c in range(cols):
        column_sum = 0
        for row in sample_list:
            column_sum += row[c]
        mylist.append(column_sum)
    return mylist