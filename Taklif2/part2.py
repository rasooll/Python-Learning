def single_insert_or_delete(s1,s2):
	if len(s1) == len(s2):
		s1 = s1.lower()
		s2 = s2.lower()
		if s1 == s2:
			return 0
		else:
			return 2
	elif (len(s1) == len(s2)-1) or (len(s1) == len(s2)+1):
		return 1
	else:
		return 2