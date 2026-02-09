nums = [3,5,6,4,8,9,10,7,1]
right=[5,6,8,8,9]
left=[1,2,4,5,6] # right=[5,6,8,8,9]

def merge(left,right):
    i,j=0,0
    result=[]
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result
def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)
print(merge_sort(nums))
