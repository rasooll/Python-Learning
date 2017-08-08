def _sort_key_ (dict):
	mylist = []
	mylist = dict.keys()
	mylist = sorted(mylist)
	return mylist
test = {'age': 21, 'name': 'rasool'}
print (_sort_key_(test))