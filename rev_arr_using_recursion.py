#reverse an array using recursion
arr = [3,2,1,5,7,36,4,32,65]
n=len(arr)-1
def rev(arr,i,n):
    if i>n:
        return 
    rev(arr,i+1,n)
    print(arr[i])
rev(arr,0,n)
