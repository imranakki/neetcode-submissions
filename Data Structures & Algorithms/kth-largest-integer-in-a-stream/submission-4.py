import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hq = nums[:k]
        heapq.heapify(self.hq)

        self.k = k
        self.nums = nums

        for i in range(k,len(nums)):
            if self.hq[0] < nums[i]:
                heapq.heappop(self.hq)
                heapq.heappush(self.hq, nums[i])

    def add(self, val: int) -> int:

        if len(self.hq) < self.k :
            heapq.heappush(self.hq, val)

        elif self.hq[0] < val:
            heapq.heappop(self.hq)
            heapq.heappush(self.hq, val)
        return self.hq[0]
