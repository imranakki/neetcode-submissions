class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        st = []

        result = [0] * n
        for i in range(n - 1, -1, -1):
            while st and t[st[-1]] <= t[i]:
                st.pop()
            
            result[i] = (st[-1] - i if st else 0)
            st.append(i)

        return result