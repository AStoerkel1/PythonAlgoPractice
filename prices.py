#given an array of prices where prices[i] is the price 
#of a given stock on the ith day find the optimal days to 
#buy and sell and return the max profit



def trade(prices: list) -> int:
    profit = 0
    buy = 10**4+1
    for x in prices:
        if x<buy:
            buy = x
        if x-buy>profit:
            profit = x-buy
    return profit

print(trade([3,3,5,0,0,3,1,4]))