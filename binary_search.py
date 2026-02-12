nums = [2,4,6,7,9,11,18,19]
def binary_search(arr,target):
    low=0
    high=len(arr) - 1
    while low<=high :
        mid = (low+high)//2
        if target==arr[mid]:
            return mid
        elif target<arr[mid]:            #  mid = 6
            high = mid - 1                #    low =  5
        else :                                    # high =   7
            low = mid + 1
    return -1
print(binary_search(nums,3))
