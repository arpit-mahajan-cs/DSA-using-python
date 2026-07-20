

# example of store freqency in dictionary 
# method 2


nums = [5,6,7,7,1,9,111,1,1,5,1,1]
hash_map =dict()
n=len(nums)
for i in range (0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
    print(hash_map)