class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        L = [0] * (n + m)
        i, j, k = 0, 0, 0
        while(i < n and j < m):
            if(nums1[i] <= nums2[j]):
                L[k] = nums1[i]
                i += 1
            else:
                L[k] = nums2[j]
                j += 1
            k += 1

        while(i < n):
            L[k] = nums1[i]
            i += 1
            k += 1

        while(j < m):
            L[k] = nums2[j]
            j += 1
            k += 1

        if(len(L) & 1):
            return float(L[len(L) // 2])
        else:
            return (L[((len(L) - 1) // 2)] + L[len(L) // 2]) / 2.0

        