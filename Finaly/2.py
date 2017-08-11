def n_letter_dictionary(my_string):
    input_list = my_string.split(" ")

    unique_set = set()
    dictionary = {}

    for item in input_list:
        word = item.lower()
        if word not in unique_set:
            unique_set.add(word)
            key = len(word)
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(word)
            dictionary[key].sort()

    return dictionary
#print(n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become"))