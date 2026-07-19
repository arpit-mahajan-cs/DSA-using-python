

# Example of brute force in optimal solution :- print all factors of a given number


num=36
from math import sqrt
result = []
for i in range (1,int(sqrt(num))+1):
    if num % i ==0:
        result.append(i)
        if num //i !=i :
            result.append (num//i)
            result.sort()
            print(result)

