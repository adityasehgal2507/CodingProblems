'''
https://leetcode.com/problems/merge-sorted-nums1ay/

You are given 
    two integer nums1ays nums1 and nums2, sorted in non-decreasing order, and 
    two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single nums1ay sorted in non-decreasing order.
The final sorted nums1ay should not be returned by the function, but instead be stored inside the nums1ay nums1. 
To accommodate this, nums1 has a length of m + n, 
    where the first m elements denote the elements that should be merged, and 
    the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.
'''
from typing import List

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         #   [1], [0]
#         #   -> [1]
#         if n == 0:
#             return nums1

#         for i in range(n):
#             nums1[i+m] = nums2[i]

#         nums1.sort()
#         print(nums1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # non decreasing = increasing
        # m and n = num of elem in nums1 and nums2 respectively

        # 
        idx = m + n - 1
        i = m - 1
        k = n - 1
        
        while i >= 0 and k >= 0:
            if nums1[i] >= nums2[k]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[k]
                k -= 1
            idx -= 1
            print(nums1)

        while k >= 0:
            nums1[idx] = nums2[k]
            k -= 1
            idx -= 1
            print(nums1)


        print('-'*50)

s = Solution()
s.merge([1, 0], 1, [2], 1)
s.merge([2, 0], 1, [1], 1)
s.merge(
    [1,2,3,0,0,0], 3, 
    [2,5,6], 3
)
s.merge(
    [4,5,6,0,0,0], 3,
    [1,2,3], 3
)