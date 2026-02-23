arr = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]
def search_rotated_sorted_array(arr,target):
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<=arr[high]:
            if arr[mid]<=target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
        else:
            if arr[low]<=target<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
    return -1
print(search_rotated_sorted_array(arr,5))
