def um_of_evens(A, B):
	sumi = 0
	for element in A:
		if (element%2) != 0:
			sumi = sumi + element
	for element in B:
		if (element%2) != 0:
			sumi = sumi + element
	return sumi