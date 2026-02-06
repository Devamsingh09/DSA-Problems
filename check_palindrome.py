#check_palindrome
# 1234
def check_palindrome(n):
    z=n
    res=0
    while n!=0:
        r = n%10
        res = res*10 + r
        n=n//10
    if res==z:
        return True
    else:
        return False
print(check_palindrome(11113931111))
        
        
