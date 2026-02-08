#reverse an array using recursion
arr = [3,2,1,5,7,36,4,32,65]
def reverse(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
    return arr
print(reverse(arr))
