def _count_of_words_sample_(simple_string):
	simple_string_list = simple_string.lower().split()
	count = 0
	for word in simple_string_list:
		if len(word) > 4:
			count = count + 1
	return count