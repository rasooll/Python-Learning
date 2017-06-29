def adadefard(a, b):
	i = a
	mylist = []
	while (i >= a) and (i <= b):
		if (i%2) != 0 :
			mylist.append(i)
		i = i+1
	mylist.sort()
	mylist.reverse()
	return mylist