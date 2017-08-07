def _2d_to_1d_list_sample_(_2d_list):
    output_list = []
    for rows in _2d_list:
        for items in rows:
            output_list.append(items)
    output_list.sort()
    return output_list