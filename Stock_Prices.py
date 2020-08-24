def solution(prices):
    length = len(prices)
    res = 0
    first = 0
    second = 0 
    
    for x in range(0, length):
        for y in range(0, length-x):
            if(res<prices[y+x]-prices[x]):
                res= prices[y+x]-prices[x]
                first = prices[x]
                second = prices[y+x]
                
        
    print(res,"is the maximum profit you can make by buying the stock when it's",first,"and selling it when it's",second)
    pass

stock = [2,4,3,-1,6,23,-3,5]
solution(stock)
