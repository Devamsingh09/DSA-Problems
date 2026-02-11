nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_subarr_sum(arr):
    n=len(arr)
    i=0
    maxi=float('-inf')
    total=0                                              
    while i<n:                                         
        total=total+arr[i]                      
        maxi=max(maxi,total)
        if total<0:
            total=0
        i+=1
    return maxi
print(max_subarr_sum(nums))
    
            
    
