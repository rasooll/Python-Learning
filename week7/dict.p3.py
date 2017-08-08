def _name_grade_(sampledict):
	keys = sampledict.keys()
	students = []
	for name in keys:
		number_list = sampledict[name]
		grade1, grade2, grade3 = number_list[0], number_list[1], number_list[2]
		if grade1 >= 78 and grade2 >= 78 and grade3 >= 78:
			students.append(name)
	return students
dict2 = {'rasool': [79, 85, 90], 'pari': [14,19,100]}
print ( _name_grade_(dict2))