def _dictionary_of_vowel_counts_sample_(sample_string):
	sample_string_nospace = sample_string.replace(' ', '')
	sample_string_nospace_lower = sample_string_nospace.lower()
	vowels_character_list = ['a', 'e', 'o', 'i', 'u']
	out_dict = {}
	for character in sample_string_nospace_lower:
		if character in vowels_character_list:
			out_dict[character] = sample_string_nospace_lower.count(character)
	return out_dict
print (_dictionary_of_vowel_counts_sample_("salam in ye payame test ast."))