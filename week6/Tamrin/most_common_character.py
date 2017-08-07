def _most_common_character_(sample_string):
    stripped_string = sample_string.replace(" ", "")
    lowercase_stripped_string = stripped_string.lower()
    sample_character = None
    sample_maximum_count = 0
    for character in lowercase_stripped_string:
        each_character_count = lowercase_stripped_string.count(character)
        if each_character_count >= sample_maximum_count:
            sample_maximum_count = each_character_count
            sample_character = character
    return sample_character