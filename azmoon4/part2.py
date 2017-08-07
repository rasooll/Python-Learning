def find_longest_word(input_string):
	maxlen = 0
	maxword = ""
	input_list = input_string.split()
	#print (input_list)
	for word in input_list:
		#print (len(word))
		if len(word) >= maxlen:
			maxlen = len(word)
			maxword = word
			#print (maxlen, maxword)
	return maxword
print (find_longest_word("salam in ye matn azmayeshi baraye test matnibebozorgiein ast"))