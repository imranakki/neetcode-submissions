class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        n = len(h)
        left = [-1] * n
        right = [n] * n
        st = []
        for i in range(n):
            while st and h[st[-1]] >= h[i]:
                st.pop()
            
            if st:
                left[i] = st[-1]
            
            st.append(i)


        st = []
        for i in range(n - 1, -1, -1):
            while st and h[st[-1]] >= h[i]:
                st.pop()
            
            if st:
                right[i] = st[-1]
            
            st.append(i)

        area = 0;
        for i in range(n):
            left[i] += 1
            right[i] -= 1
            area = max(area, h[i] * (right[i] - left[i] + 1))
        return area




