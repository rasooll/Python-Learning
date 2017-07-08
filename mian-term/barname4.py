# Type your code here
def crazy_list(some_list):
  mylist = some_list
  lenlist = len(mylist)
  aval = 0
  akhar = -1
  natije = 0
  for i in range(0,lenlist):
  	if mylist[aval] != mylist[akhar]:
  		natije = natije + 1
  	aval = aval + 1
  	akhar = akhar - 1
  if natije == 0:
  	return True
  else:
  	return False
listam = [5, 6, 8, 7, 'PYTHON', 9, 8, 6, 5]
print (crazy_list(listam))