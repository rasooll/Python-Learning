def find_word_horizontal(crosswords,word):
    if not crosswords or not word : # if empty then return None
        return None
    for index,row in enumerate(crosswords):
        temp_str=''.join(row)
        if temp_str.find(word)>=0:
            return [index,temp_str.find(word)]
    return None
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(find_word_horizontal(crosswords,word))