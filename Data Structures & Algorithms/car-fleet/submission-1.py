class Solution:
    def carFleet(self, target: int, p: List[int], s: List[int]) -> int:
        car = [(p[i], s[i]) for i in range(len(p))]
        car = sorted(car, key = lambda x: -x[0])
        st = []
        for i in range(len(car)):
            x = (target - car[i][0]) / car[i][1]
            st.append(x)
            while(len(st) >= 2 and st[-1] <= st[-2]):
                st.pop()
            
        return len(st)
        """
        [4, 2, 0]  => (6, 8/3, 5)
        [1, 3, 2]
        """