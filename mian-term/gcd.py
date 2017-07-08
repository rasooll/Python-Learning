# Type your code here
def find_gcd(my_list):

    L = list(my_list)

    while len(L) > 1:
        a = L[len(L) - 2]
        b = L[len(L) - 1]
        L = L[:len(L) - 2]
        
        while a:
            a, b = b%a, a

        L.append(b)
        
    return abs(b)
aa = [3, 5, 9, 11, 13]
print (find_gcd(aa))