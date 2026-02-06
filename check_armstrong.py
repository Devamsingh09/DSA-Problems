# n = 153
import math
def leng(n):
    c=0
    while n!=0:
        if n==0:
            return 1
        n=n//10
        c+=1
    return c
    
def check_armstrong(n):
    z=n
    s=0
    p = leng(n)
    while n!=0:
        r = n%10
        s = s + math.pow(r,p)
        n = n//10
    if s==z:
        return True 
    else:
        return False
print(check_armstrong(153))
        
    
