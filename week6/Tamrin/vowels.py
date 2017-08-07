def _vowels_ (simple_string):
	number = 0
	simple_string = simple_string.lower()
	vowels_character_list = ['a', 'e', 'o', 'i', 'u']
	for char in simple_string:
		if char in vowels_character_list:
			number = number + 1
	return number