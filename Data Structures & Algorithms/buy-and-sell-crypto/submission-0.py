class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxP = 0,1, 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            currP= prices[r] - prices[l]
            maxP = max(maxP, currP)
        return maxP
        