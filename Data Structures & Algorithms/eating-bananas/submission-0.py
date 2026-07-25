class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(k):
            hh = 0
            for i in piles:
                hh += (i + k - 1) // k
            return hh <= h

        l = 1
        r = sum(piles)
        ans = -1
        while (l <= r):
            m = (l + r) >> 1
            if can(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans