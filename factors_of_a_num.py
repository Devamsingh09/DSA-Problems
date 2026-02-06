result= []
import math
def print_factors(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n%i==0:
            result.append(i)
            if n//i!=i:
                result.append(n//i)
    
    print(result)
print_factors(26)
