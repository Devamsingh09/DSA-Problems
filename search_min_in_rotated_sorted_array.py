arr = [7,8,1,2,3,4,5,6]
arr1=[4,5,6,7,0,1,2]
def search_min_in_rotated_sorted_array(arr):
    n=len(arr)
    low,high=0,n-1
    mini=float('inf')
    while low<=high:
        mid = (low+high)//2
        if arr[low]<=arr[mid]:
            mini=min(mini,arr[low])
            low=mid+1
        else:
            mini=min(mini,arr[low])
            high=mid-1
    return mini
print(search_min_in_rotated_sorted_array(arr))
