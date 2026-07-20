

# Example of hasing in optimal solution using hash list 


n=[5,3,2,2,1,5,5,7,5,10]

m=[10,111,1,9,5,67,2]

hash_list = [0,1,2,1,0,4,0,1,0,0,1]
hash_list = [0]*11
for num in n:
    hash_list[num]+=1
    for num in m :
        if num>10:
            print(0)
        else:
            print(hash_list[num])