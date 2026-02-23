#min index suh that:  arr[i]>=target
arr= 1,1,1,2,3,3,5,6,7,7,7,9,12,12,13    # target =3 , high=6
def lower_bound(arr,target):
    n=len(arr)
    lb=n
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2             #target =6 , high =7  , low = 6, mid = 5
        if arr[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return mid
print(lower_bound(arr,1))
            
        
