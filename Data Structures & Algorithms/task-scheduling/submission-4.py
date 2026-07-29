import heapq
from collections import defaultdict, deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cd = deque([])
        m = Counter(tasks)
        heap_mx = [-v for v in m.values()]
        heapq.heapify(heap_mx)
        ans = 0
        while heap_mx or cd:
            if not heap_mx and cd:
                t = cd.popleft()
                ans = t[0]
                heapq.heappush(heap_mx, t[1])

            while cd and ans == cd[0][0]:
                t = cd.popleft()
                heapq.heappush(heap_mx, t[1])
            
            e = heapq.heappop(heap_mx)
            if -e > 1:
                cd.append((ans + n + 1, e + 1))
            ans += 1

        return ans
            

        
            

                

