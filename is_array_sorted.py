nums=[33,23,54,67,76,95]
arr=[34,34,34,45,56,67,77]
def is_sorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
            break
    return True
print(is_sorted(arr))
            
            
        
