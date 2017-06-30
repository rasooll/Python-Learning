def reverse_of_a_list(A):
	newlist = []
	for i in range(0, len(A)):
		newlist.append(A[-1])
		del A[-1]
	return newlist
input_list = ['apples', 'eat', "don't", 'I', 'but', 'Grapes', 'Love', 'I']
print (reverse_of_a_list(input_list))