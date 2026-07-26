from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sl = SortedList([])
        ans = []
        for i in range(k):
            sl.add(nums[i])
        
        ans.append(sl[-1])
        for i in range(k, len(nums)):
            sl.remove(nums[i - k])
            sl.add(nums[i])
            ans.append(sl[-1])

        return ans


        