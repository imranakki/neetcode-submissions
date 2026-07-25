class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for e in nums:
            if e in s:
                return e
            s.add(e)
        