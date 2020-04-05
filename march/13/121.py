class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        minprice = max(prices)
        maxprofit  = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit
    
                
#         k = 0
#         for i in range(0,len(prices)-1):
#             a = max(prices[i+1:])
#             k = max(k,a - prices[i])
#         return k
