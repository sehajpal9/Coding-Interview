# given an array of prices of a stock per day, return the max profit you can get if you buy the stock on one day and sell it in a future day
# for example: input = [7,1,5,3,6,4] output = 5 because buy for 1 and sell for 6 ... input = [7,6,4,3,1] output = 0 because cant make a positive profit 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 1 or len(prices) > 10**5:
            return 0
        # prices[i] = given stock on ith day
        # single day to buy and future day to sell

        # max profit = buy at lowest possible price and sell at highest possible price 

        min_price = prices[0]
        profit = 0

        for price in prices:
            print(price, " ", min_price)
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price

        return profit


# alternative approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_p = inf
        max_p = 0
        profit = 0
        
        for i, price in enumerate(prices):
            if price < min_p:
                min_p = price
            elif (price - min_p) > profit:
                max_p = price 
                profit = max_p - min_p
            #print("min: ", min_p, "max: ", max_p, "profit= ", profit)
        
        return profit 
