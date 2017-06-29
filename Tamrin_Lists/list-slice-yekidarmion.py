def slice(mylist):
	outlist = []
	outlist.append(mylist[0])
	tool = len(mylist)
	for i in range(1, tool):
		if (i%2) == 0:
			outlist.append(mylist[i])
	return outlist