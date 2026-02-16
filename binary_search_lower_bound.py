arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
def lower_bound(arr,target):
    n=len(arr)
    lb=n
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
print(lower_bound(arr,11))
print(arr[lower_bound(arr,13)])
