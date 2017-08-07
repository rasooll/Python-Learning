def _count_even_sum_sample_(sample_2d_list):
    even_count = 0
    odd_count = 0
    # For each row
    for rows in sample_2d_list:
        row_sum = sum(rows)
        if row_sum % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return [even_count, odd_count]