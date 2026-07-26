class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        cs = set(s)
        ans = 0
        for c in cs:

            l = 0
            r = 0
            cnt = 0
            while r < n:
                if s[r] == c:
                    cnt += 1

                while((r - l + 1 - cnt) > k):
                    if(s[l] == c): cnt -= 1
                    l += 1

                ans = max(ans, r - l + 1)
                 
                r += 1  
        return ans