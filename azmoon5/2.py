def construct_dictionary_from_lists(names, ages, scores):
	lengh = len(names)
	out_dict = {}
	for item in range (0, lengh):
		status = ''
		if scores[item] >= 60:
			status = "pass"
		else:
			status = "fail"
		itemlist = []
		itemlist.append(ages[item])
		itemlist.append(scores[item])
		itemlist.append(status)
		out_dict[names[item]] = itemlist
	return out_dict

one = ["paul", "saul", "steve", "chimpy"]
two = [28, 59, 22, 5]
three = [59, 85, 55, 60]
print(construct_dictionary_from_lists(one,two,three))