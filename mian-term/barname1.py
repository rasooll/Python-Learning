# Type your code here
def find_integer_with_most_divisors(input_list):
  mylist = []
  len_list = int(len(input_list))
  for i in range (0,len_list+1):
  	count = 0
  	y = input_list[i]
  	for x in range(1,y):
  		if (input_list[i]%x) == 0:
  			count = count + 1
  	mylist.append (count)
  return count
test = [8, 12, 18, 6]
print (find_integer_with_most_divisors(test))