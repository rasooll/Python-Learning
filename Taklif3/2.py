def find_word_horizontal(crossword,word):
    for row_index, row in enumerate(crossword):
        row_string = ''.join(row)
        column_index = row_string.find(word)
        if(column_index > -1):
            return [row_index, column_index]

def find_word_vertical(crossword,word):
    z=[list(i) for i in zip(*crossword)]   
    for rows in z:          
        row_index = z.index(rows)
        single_row = ''.join(rows)      
        column_index = single_row.find(word)        
        if column_index >= 0:
            return([column_index, row_index])

def capitalize_word_in_crossword(crossword,word):
     i_v=-1
     j_v=-1
     i_h=-1
     j_h=-1
     index_cap = find_word_horizontal(crossword,word)
     if index_cap is not None:
        i_h,j_h=index_cap
     else:
        index_cap = find_word_vertical(crossword,word)
        if index_cap is not None:
           i_v,j_v=index_cap


     for row_index in range(len(crossword)):
         for col_index in range(len(crossword[row_index])):

             for w in range(len(word)):
                 if i_h is not -1:                       
                    if row_index==i_h and col_index==j_h+w:
                       crossword[row_index][col_index] = (crossword[row_index][col_index]).upper()

                 if i_v is not -1:
                    if row_index==i_v+w and col_index==j_v:
                       crossword[row_index][col_index] = (crossword[row_index][col_index]).upper()
                    else:
                       crossword[row_index][col_index] = (crossword[row_index][col_index])

     return (crossword)
crossword=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(capitalize_word_in_crossword(crossword,word))