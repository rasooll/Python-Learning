def _handle_concatenation_error_sample_(unknown, string):
    try:
        result = unknown + string
    except TypeError:
        return None
    else:
        return result
  