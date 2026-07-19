

# Example of brute force  in better solution :- Print all factores of a given number

num = 10
result = []
for i in range (1,num//2):
    if num % i ==0 :
        result.append(i)
        result.append(num)
        print(result)

