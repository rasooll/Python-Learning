def anagrams(my_string1, my_string2):
	#count = 0
	my_string1 = my_string1.lower()
	my_string2 = my_string2.lower()
	my_string2 = sorted(my_string2)
	my_string1 = sorted(my_string1)
	#for char in my_string1:
	#	if char not in my_string2:
	#		count = count + 1
	#if count == 0:
	#	return True
	#else:
	#	return False
	print (my_string1 , my_string2)
	if my_string1 == my_string2:
		return True
	else:
		return False
print (anagrams('Carthorse', "Orchestra"))