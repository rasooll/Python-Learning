def list_manipulation(mylist):
	newlist = mylist[:]
	del newlist[0]
	del newlist[-1]
	return newlist