def find_word_vertical(crosswords,word):
	z=[list(i) for i in zip(*crosswords)]   
	for rows in z:          
		row_index = z.index(rows)
		single_row = ''.join(rows)      
		column_index = single_row.find(word)        
		if column_index >= 0:
			break
	return([column_index, row_index])
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(find_word_vertical(crosswords,word))