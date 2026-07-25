class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        l, r = 0, n * m - 1;
        while l <= r:
            md = (l + r) >> 1
            i = md // m
            j = md % m
            
            if(matrix[i][j] == target):
                return True
            elif matrix[i][j] < target:
                l = md + 1
            else:
                r = md - 1
        
        return False