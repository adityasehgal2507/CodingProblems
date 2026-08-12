'''
Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. 
If not, 
    return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

from typing import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums)
        while b-a > 1:
            c = (a + b) // 2
            if nums[c] == target:
                return c
            elif nums[c] > target:
                b = c
            else:
                a = c

        return a if nums[a] >= target else b

def run_tests():
    sol = Solution()
    test_cases = [
        {"nums": [1, 3, 5, 6], "target": 5, "expected": 2, "desc": "Target exists in middle"},
        {"nums": [1, 3, 5, 6], "target": 2, "expected": 1, "desc": "Insert in middle"},
        {"nums": [1, 3, 5, 6], "target": 7, "expected": 4, "desc": "Insert at end"},
        {"nums": [1, 3, 5, 6], "target": 0, "expected": 0, "desc": "Insert at beginning"},
        {"nums": [1], "target": 1, "expected": 0, "desc": "Single element, match"},
        {"nums": [2], "target": 1, "expected": 0, "desc": "Single element, insert before"},
        {"nums": [1], "target": 2, "expected": 1, "desc": "Single element, insert after"},
        {"nums": [-10, -5, 0, 3, 8], "target": -2, "expected": 2, "desc": "Negative and zero bounds"}
    ]
    
    print(f"{'Description':<30} | {'Passed':<6}")
    print("-" * 40)
    for tc in test_cases:
        result = sol.searchInsert(tc["nums"], tc["target"])
        passed = result == tc["expected"]
        print(f"{tc['desc']:<30} | {str(passed):<6} (Got {result}, Expected {tc['expected']})")
        print("-" * 40)

if __name__ == "__main__":
    run_tests()
