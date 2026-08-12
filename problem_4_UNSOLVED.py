'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
    return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''

from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Disjoint sliding window of size 2
        Window can exist in either single array or disjoint across 2 arrays
        '''

test_cases = [
    # nums1, nums2, expected median

    # Basic cases
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),

    # One array is empty
    ([], [1], 1.0),
    ([1], [], 1.0),
    ([], [1, 2], 1.5),
    ([1, 2], [], 1.5),

    # Single elements
    ([1], [2], 1.5),
    ([2], [1], 1.5),

    # Odd total length
    ([1, 3], [2, 4, 5], 3.0),
    ([1, 2, 3], [4, 5], 3.0),

    # Even total length
    ([1, 2], [3, 4], 2.5),
    ([1, 2, 3, 4], [5, 6], 3.5),

    # Duplicate values
    ([1, 1], [1, 1], 1.0),
    ([1, 2, 2], [2, 3, 3], 2.0),

    # Negative numbers
    ([-5, -3, -1], [-4, -2], -3.0),
    ([-2, -1], [1, 2], 0.0),

    # Mixed negative and positive
    ([-5, -3, 0], [1, 2, 4], 0.5),

    # Very different ranges
    ([1, 2, 3], [100, 101, 102], 51.5),
    ([100, 101], [1, 2, 3], 3.0),

    # One array contains all smaller values
    ([1, 2, 3], [4, 5, 6], 3.5),

    # One array contains all larger values
    ([4, 5, 6], [1, 2, 3], 3.5),

    # Zeros
    ([0, 0], [0, 0], 0.0),
    ([-1, 0], [0, 1], 0.0),

    # Localized Median
    ([1, 2, 10, 11], [3, 4, 5], 4)
    ([1, 2, 10, 11], [3, 4, 5, 6], 4.5)
]

solution = Solution()

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

for nums1, nums2, expected in test_cases:
    try:
        got = solution.findMedianSortedArrays(nums1, nums2)

        if got == expected:
            print(f"{GREEN}[PASS]{RESET} Expected: {expected} Got: {got}")
        else:
            print(f"{RED}[FAIL]{RESET} Expected: {expected} Got: {got}")

    except Exception as error:
        print(f"{RED}[FAIL]{RESET} Expected: {expected} Got: error - {error}")