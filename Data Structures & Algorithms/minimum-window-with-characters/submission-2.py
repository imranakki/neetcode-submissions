from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def check():
            ok = True
            for e in st:
                ok &= (e in mp and e in mpO and mp[e] >= mpO[e])
            return ok

        st = set(t)
        mp = dict()
        mpO = dict(Counter(t))

        ans = float("inf")
        bl, br = None, None

        l = 0
        for r in range(len(s)):
            if s[r] not in st:
                continue
            
            mp[s[r]] = mp.get(s[r], 0) + 1

            
            
            while check():
                
                if ans > (r - l + 1):
                    ans = r - l + 1
                    bl = l
                    br = r

                if s[l] in st:
                    mp[s[l]] -= 1
                l += 1
            

        
       


                
        print(bl, br)
        return  s[bl:br + 1] if (bl is not None) and (br is not None) else ""