nums=[33,23,54,67,76,95]

def right_rotate_arr_by_one(arr):
    n=len(arr)
    i=len(arr)-1
    temp=arr[n-1]
    while i>=1:
        arr[i]=arr[i-1]
        i-=1
    arr[i]=temp
    return arr
        
        
print(right_rotate_arr_by_one(nums))
            
            
        
