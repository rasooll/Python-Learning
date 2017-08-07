def _preserve_and_reverse_sample_(string):
    splitted_list = string.split()
    for x in range(0, len(splitted_list)):
        splitted_list[x] = splitted_list[x][::-1]
    # Initialize an output string
    output_string = ""
    for x in range(0, len(splitted_list)):
        output_string += splitted_list[x] + " "
    # Strip any white spaces
    output_string = output_string.strip()
    return output_string