def _number_of_char_in_string_ (simple_string,simple_char):
	count = 0
	simple_string = simple_string.lower()
	for char in simple_string:
		if char == simple_char:
			count = count + 1
	return count