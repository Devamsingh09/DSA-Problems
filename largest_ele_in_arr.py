# largest ele in array :
arr = [2,3,54,13,55,89,56]
def largest_element(arr):
    lg=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>lg:
            lg=arr[i]
    return lg
        
# TC: O(n)
    
print(largest_element(arr))
