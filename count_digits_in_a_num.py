# count num of digits in an integer
# n= 89324
def count(n):
    if n==0:
        return 1
    c=0
    while n!=0:
        n=n//10
        c+=1
    return c
print(count(1))
        
        
        
    
