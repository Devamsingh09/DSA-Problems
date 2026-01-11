arr = [1,2,3,21,54,5]

def check_duplicates(arr):
    seen = set()
    for i in range(0,len(arr)):
        if arr[i] in seen:
            return True 
            break
        seen.add(arr[i])
    return False
print(check_duplicates(ar))
  
print(check_duplicate(arr))
#     TC: O(n)
#     SC: O(n)
