def _reverse_string_sample_(sample_string):
    output = ""
    i = -1
    # iterate the list from end to the front
    while i != (- (len(sample_string) + 1)):
        output = output + sample_string[i].swapcase()
        i = i - 1
    return output