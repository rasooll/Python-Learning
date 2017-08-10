def one_to_2D(some_list, r, c):
    result = []
    #print(str(some_list).strip('[]').replace(', ', ''))
    lengh = len(some_list)
    if (r*c > lengh):
    	for i in range(1, r+1):
        	result.append(some_list[c*(i-1):c*i])
    	return result
    else:
    	for i in range(1, r+1):
        	result.append(some_list[c*(i-1):c*i])
    	return result
print( one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3))