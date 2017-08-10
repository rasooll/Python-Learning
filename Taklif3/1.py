def find_word_vertical(crosswords,word):
    if not crosswords or not word:
        return None    
    number_of_columns=len(crosswords[0])
    for col_index in range (number_of_columns):
        temp_str=''
        for row_index in range(len(crosswords)):
            temp_str=temp_str+crosswords[row_index][col_index]
        if temp_str.find(word)>=0:
            return [temp_str.find(word),col_index]
    return None
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(find_word_vertical(crosswords,word))