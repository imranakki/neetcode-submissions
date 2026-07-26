from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        mp = dict(Counter(s1))
        curr = dict()
        l = 0
        for r in range(n):
            
            curr[s2[r]] = curr.get(s2[r], 0) + 1

            while(r - l + 1 > len(s1)):
                curr[s2[l]] -= 1
                if not curr[s2[l]]:
                    del curr[s2[l]]
                l += 1

            if curr == mp:
                return True
            
            print(curr)
            
        return False