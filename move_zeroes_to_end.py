nums=[1,0,2,4,3,0,0,3,5,1]

def move_zeroes_to_right(arr):
    n=len(arr)
    i,j=0,1
    while j<n:
        if arr[i]!=0:
            j+=1
            i+=1
        elif arr[i]==0 and arr[j]==0:
            j+=1
        else:
            #arr[i]==0 and arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
            i+=1
move_zeroes_to_right(nums)
print(nums)
        
        
        
        
            
            
        
