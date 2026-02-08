ist=[]
def fibb(n):
    if n == 0 or n==1:
        return n
    
    return fibb(n-1) + fibb(n-2)
    list.append(n)
print(fibb(5))

