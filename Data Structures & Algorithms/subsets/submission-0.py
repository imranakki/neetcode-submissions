class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range((1 << n)):
            x = []
            for j in range(n):
                if i & (1 << j): x.append(nums[j])
            ans.append(x)
        return ans