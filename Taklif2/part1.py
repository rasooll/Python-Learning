def find_mismatch(s1,s2):
	s1 = s1.lower()
	s2 = s2.lower()
	if len(s1) == len(s2):
		count = 0
		for x in range (0, len(s1)):
			if s1[x] != s2[x]:
				count = count + 1
		if count == 0:
			return 0
		elif count == 1:
			return 1
		else:
			return 2
	else:
		return 2