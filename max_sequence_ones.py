nums = [1,1,0,1,0,1,1,1,1,0,1,1]
def max_ones(arr):
    sum=0
    max_sum=0
    i,j=0,0
    while i<len(arr):
        if arr[i]==0:
            i+=1
            max_sum=max(max_sum,sum)
            sum=0
        else:
            sum=sum+1
            i+=1
    return max_sum
print(max_ones(nums))
            
        
max_ones(nums)
        
        
        
    
            
        
    
