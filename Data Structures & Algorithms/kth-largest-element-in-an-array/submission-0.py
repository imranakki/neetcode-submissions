import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for e in nums:
            if len(heap) == k:
                if heap[0] < e:
                    heapq.heappop(heap)
                    heapq.heappush(heap, e)
            else:
                heapq.heappush(heap, e)
        
        return heap[0]
