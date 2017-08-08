numbers={"one": "uno", "two": "dos", "three": "tres"}
print ("uno"  in numbers)

#numbers={"one": "uno", "two": "dos"}
#numbers["two"]=1
#print (numbers["dos"])

numbers={"one": "uno", "two": "dos"}
numbers["dos"]="two"
print (numbers["two"])

numbers={"one": 1, "two": [4, 6, 3], "three": 3}
x = (numbers["two"])
x.sort()
print(x)