class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) >> 1
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
            
        split = l
        print(split)
        l = 0 if target > nums[-1] else split
        r = split - 1 if target > nums[-1] else len(nums) - 1

        while l <= r:
            m = (l + r) >> 1
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

