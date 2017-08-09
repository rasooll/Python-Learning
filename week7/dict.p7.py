def _dictionary_of_word_counts_sample_(sample_string):
	sample_string_lower = sample_string.lower()
	sample_list = sample_string_lower.split()
	out_dict = {}
	for character in sample_list:
		out_dict[character] = sample_string_lower.count(character)
	return out_dict
print (_dictionary_of_word_counts_sample_('I am tall when I am young and I am short when I am old'))