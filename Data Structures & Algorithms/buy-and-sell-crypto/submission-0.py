class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = prices[-1]
        ans = 0

        for i in range(len(prices) - 2, -1, -1):
            ans = max(ans, mx - prices[i])
            mx = max(mx, prices[i])

        return ans