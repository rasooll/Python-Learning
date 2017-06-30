def list_manipulation(mylist):
	num=o
	for i in mylist:
		if (i%2) != 0:
			x = mylist[num] + 1
			mylist[num] = x
		num = num+1
	return mylist
