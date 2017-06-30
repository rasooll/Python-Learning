def __2to4__(mylist, st):
	del mylist[1:4]
	i=0
	for i in range(3):
		mylist.insert(1, st)
	return mylist
list2 = ["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"]
inp = "bahram"
print (__2to4__(list2, inp))