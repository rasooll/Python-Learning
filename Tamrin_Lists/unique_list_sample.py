def unique_list_sample(mylist):
	newlist = []
	for element in mylist:
		if element not in newlist:
			newlist.append(element)
	return newlist