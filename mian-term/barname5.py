# Type your code here
def pattern_sum(a, b):
	sumi = 0
	i=1
	mylist = []
	while i <= b:
		javab = (sumi*10+a)
		sumi = javab
		i = i + 1
		mylist.append(sumi)
	tool = len(mylist)
	sumii = 0
	i=0
	while i < tool:
		sumii = sumii + mylist[i]
		i = i+1
	return sumii
print (pattern_sum(4, 5))