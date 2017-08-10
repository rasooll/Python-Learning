x = input("Please enter something: ")
try:
    x = int(x)
except ValueError:
    print('Error')
else:
    print(x)
  