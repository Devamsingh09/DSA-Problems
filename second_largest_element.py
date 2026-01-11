# largest ele in array :
arr = [2,3,54,13,55,89,56,66]
def sec_largest_element(arr):
    lg = float('-inf')
    slg = float('-inf')
    for i in range(0,len(arr)):
        if arr[i]>lg:
            slg=lg
            lg=arr[i]
        elif arr[i]>slg and arr[i]!=lg:
            slg=arr[i]
    if slg!=float('-inf'):
        return slg
    else:
        return -1

        
# TC: O(n)
    
print(sec_largest_element(arr))
