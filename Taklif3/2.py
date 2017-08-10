def capitalize_word_in_crossword(crosswords,word):
     i_v=-1
     j_v=-1
     i_h=-1
     j_h=-1
     index_cap = find_word_horizontal(crosswords,word)
     if index_cap is not None:
        i_h,j_h=index_cap
     else:
        index_cap = find_word_vertical(crosswords,word)
        if index_cap is not None:
           i_v,j_v=index_cap


     for row_index in range(len(crosswords)):
         for col_index in range(len(crosswords[row_index])):

             for w in range(len(word)):
                 if i_h is not -1:                       
                    if row_index==i_h and col_index==j_h+w:
                       crosswords[row_index][col_index] = (crosswords[row_index][col_index]).upper()

                 if i_v is not -1:
                    if row_index==i_v+w and col_index==j_v:
                       crosswords[row_index][col_index] = (crosswords[row_index][col_index]).upper()
                    else:
                       crosswords[row_index][col_index] = (crosswords[row_index][col_index])

     return (crosswords)
