nums=[33,23,54,67,76,95]
arr=[34,34,34,45,56,67,77]
def remove_duplicates(arr):
    n=len(arr)
    i,j=0,1
    while j<n:
        if arr[j]!=arr[i]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
        
    if len(arr)==1:
        return 1
    return i+1
        
    
print(remove_duplicates(arr))
            
            
        
