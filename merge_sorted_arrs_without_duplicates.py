nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9,10]

def merge(arr1,arr2):
    result=[]
    i,j=0,0
    n1,n2=len(arr1),len(arr2)
    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            if not result or result[-1]!=arr1[i]:
                result.append(arr1[i])
            i+=1
        else:
            if not result or result[-1]!=arr2[j]:
                result.append(arr2[j])
            j+=1
    if i<n1:
        while i<n1:
            if not result or result[-1]!=arr1[i]:
                result.append(arr1[i])
            i+=1
    else:
        while j<n2:
            if not result or result[-1]!=arr2[j]:
                result.append(arr2[j])
            j+=1
    return result
result = merge(nums1,nums2)
print(result)
