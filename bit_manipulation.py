def start_to_goal(start,goal):
    ans=start^goal
    count=0
    for i in range(0,32):
        if ans&(1<<i)!=0:
            count+=1
    return count
    
    
print(start_to_goal(10,7))
arr=[5,1,3,3,7,1,7]
def find_single_number(arr):
    ans=0
    for num in arr:
        ans=ans^num
    return ans
print(find_single_number(arr))


nums=[1,2,3]
def generate_subsets(nums):
    n=len(nums)
    total_subsets=1<<n
    result=[]
    for num in range(0,total_subsets):
        lst=[]
        for i in range(0,n):
            if num&(1<<i)!=0:
                lst.append(nums[i])
        result.append(lst)
    return result
print(generate_subsets(nums))
