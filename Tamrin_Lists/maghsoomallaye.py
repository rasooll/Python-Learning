def maghsoom(k):
	i = 1
	mylist = []
	while (i >= 1) and (i <= k):
		if (k%i) == 0:
			mylist.append(i)
		i = i+1
	return mylist