arr = [1,2,3,21,54,5]

def check_duplicate(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]==arr[i]:
                return True
                break
    return False
  
print(check_duplicate(arr))
#     TC: O(n)
#     SC: O(n)
