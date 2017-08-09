def _return_keys_list_sample_(sample_dictionary, sample_value):
	out_list = []
	for key in sample_dictionary.keys():
		if sample_value in sample_dictionary[key]:
			out_list.append(key)
	return out_list