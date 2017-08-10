def _handle_index_error_(my_list, index, string):
    try:
        my_list[index] = string
    except (IndexError, TypeError):
        return my_list
    else:
        return my_list