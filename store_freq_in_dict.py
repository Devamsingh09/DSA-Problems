
nums = [5,6,7,7,1,9,111,1,1,5,1,1]

freq_map = dict() # or {}
c=1
for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1
print(freq_map)
    
