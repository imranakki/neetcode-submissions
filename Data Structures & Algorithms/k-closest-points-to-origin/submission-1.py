import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap  = []
        for e in points:
            d2 = e[0] * e[0] + e[1] * e[1]
            if len(heap) == k:
                if heap[0][0] < -d2:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-d2, e))
            else:
                heapq.heappush(heap, (-d2, e))
        return [e[1] for e in heap]