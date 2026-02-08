nums = [55,67,58,34,12,61,912,23]

def insertion_sort(arr):
    n=len(arr)
    for i in range(0,n):
        min_id=i
        for j in range(i+1,n):
            if arr[j]<arr[min_id]:
                min_id=j
        arr[min_id],arr[i]=arr[i],arr[min_id]
    return arr
print(insertion_sort(nums))
