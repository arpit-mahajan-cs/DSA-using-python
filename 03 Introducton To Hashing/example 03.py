

#  Example of number hashing  using Dictionaries instead


n=[5,3,2,2,1,5,5,7,5,10]

m=[10,111,1,9,5,67,2]

freq_dict = []
freq_dict = [0]*11
for num in n:
    freq_dict[num]+=1
    for num in m:
        if num<1 or num>10:
            print(0)
        else:
            print(freq_dict[num])