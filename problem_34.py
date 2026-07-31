from typing import List

class Solution:
    def binarySearch(self, nums, target, findFirst):
        start, end = 0, len(nums) - 1
        occurrence = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                occurrence = mid
                if findFirst:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return occurrence

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]