'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
https://leetcode.com/problems/reverse-integer
'''

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        is_neg = x < 0
        x = abs(x)
        while x > 0:
            if x < -214748365 or x > 214748364:
                return 0
            rev = (rev * 10) + (x % 10)
            x //= 10
        return rev * (-1 if is_neg else 1)

print(Solution().reverse(2**29 - 1))