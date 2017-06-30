def unique_list_sample(A, B):
	mylist = A + B
	newlist = []
	for element in mylist:
		if element not in newlist:
			newlist.append(element)
	return newlist