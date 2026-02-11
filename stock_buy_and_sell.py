nums = [7,2,1,5,6,4,8]

def stock_buy_and_sell(arr):
    n=len(arr)
    max_profit=0
    min_cost=float('inf')
    profit,i=0,0
    hash_buy=dict()
    while i<n:
        if arr[i]<min_cost:                                                       # arr[i]    = 8
            min_cost=arr[i]                                                             #  min= 1
        profit = arr[i] - min_cost                                               #  pro    = 7
        max_profit=max(max_profit,profit)                # max_proft    = 7
        i+=1
    return max_profit
            
    
print(stock_buy_and_sell(nums))
    
            
    
