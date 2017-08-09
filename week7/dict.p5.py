def _dictionary_of_letter_counts_sample_(sample_string):
	sample_string_nospace = sample_string.replace(' ', '')
	sample_string_nospace_lower = sample_string_nospace.lower()
	out_dict = {}
	for char in sample_string_nospace_lower:
		out_dict[char] = sample_string_nospace_lower.count(char)
	return out_dict