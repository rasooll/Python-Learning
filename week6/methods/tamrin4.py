def rasool(string):
	output = ""
	for x in range(0, len(string)):
		if string[x] != " ":
			output = output + string[x]
	return output
print (rasool("fdsf  safsaf safas 1233"))