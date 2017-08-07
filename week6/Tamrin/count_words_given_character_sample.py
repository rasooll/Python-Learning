def _count_words_given_character_sample_ (simple_string,simple_character):
	simple_string = simple_string.lower().split()
	simple_character = simple_character.lower()
	count = 0
	for word in simple_string:
		if word[0] == simple_character:
			count = count + 1
	return count