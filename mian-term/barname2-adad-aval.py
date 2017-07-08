# Type your code here
def list_of_primes(n):
	def isprime(r):
	    r = abs(int(r))
	    if r < 2:
	        return False
	    if r == 2: 
	        return True    
	    if not r & 1: 
	        return False
	    for x in range(3, int(r**0.5)+1, 2):
	        if r % x == 0:
	            return False
	    return True
	#print(isprime(n))
	i=1
	mylist=[]
	while i < n:
		prim = isprime(i)
		if prim:
			mylist.append(i)
		i = i + 1
	return mylist
	    

print(list_of_primes(99))