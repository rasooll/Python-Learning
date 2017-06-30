def list_manipulation(mylist, k):
	mycount = 0
	for i in mylist:
		if i == k:
			mycount = mycount + 1
	return mycount