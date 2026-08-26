class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        l, r = 0, 1
        while r < n:
            buy = prices[l]
            sell = prices[r]
            if (sell - buy) < 0:
                l = r
            elif (sell - buy) > max_profit:
                max_profit = sell - buy
                
            r += 1
        
        return max_profit
            