def _handle_division_error_(my_float, unknown):
    try:
        result = my_float / unknown
    except (ZeroDivisionError, TypeError):
        return None
    else:
        return result