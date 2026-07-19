

# Example of brute force :- Print all the factors of a given number

num = 20
result = []
for i in range(1,num+1):
    if num % i == 0:
        result.append(i)
        print (result)
