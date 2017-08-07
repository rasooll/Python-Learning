def _max_of_columns_sample_(sample_list):
    cols = len(sample_list[0])
    mylist = []
    for c in range(cols):
        column_max = 0
        for row in sample_list:
            if row[c] > column_max:
                column_max = row[c]
        mylist.append(column_max)
    return mylist