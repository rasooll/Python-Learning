# Type your code here
def items_price(a, b):
  tool = len(a)
  i = 0
  sum = 0
  while i < tool:
  	zarb = 0
  	zarb = a[i] * b[i]
  	sum = sum + zarb
  	i = i + 1
  return sum

lista=[2, 3, 5, 7, 9]
listb=[5, 8, 4, 1, 11]
print (items_price(lista, listb))