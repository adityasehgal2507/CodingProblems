'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
    return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''

from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size = (len(nums1) + len(nums2))
        i1, i2 = 0, 0
        while i1 + i2 < (size//2) - (size%2) - 1:
            if nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                i1 += 1

        if size % 2 == 1:
            return max(nums1[i1], nums2[i2])
        else:
            return (nums1[i1] + nums2[i2]) * 0.5

print(Solution().findMedianSortedArrays(
    [1, 2], [3, 4]
))

print(Solution().findMedianSortedArrays(
    [1, 3], [2]
))