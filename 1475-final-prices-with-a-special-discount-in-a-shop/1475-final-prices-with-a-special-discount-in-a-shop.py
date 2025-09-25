class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                if j>i and prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices
        