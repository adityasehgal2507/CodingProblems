'''
Extension of problem 66
Add two multidigit number writter as lists

eg. 
    [1, 0] + [9] = [1, 9]
    [9, 9] + [1, 1] = [1, 1, 0]
    [9, 5, 6] + [1, 2, 3] = [1, 0, 7, 9]
'''

from typing import List

# class Solution:
#     def plus(self, num1: List[int], num2: List[int]) -> List[int]:
#         larger = num1 if len(num1) > len(num2) else num2
#         smaller = num1 if len(num1) <= len(num2) else num2

#         smaller = [0 for _ in range(len(larger) - len(smaller))] + smaller

#         carry = 0
#         for i in range(len(larger)-1, -1, -1):
#             s = larger[i] + smaller[i] + carry
#             carry = s // 10
#             larger[i] = s % 10
#         if carry:
#             larger = [1] + larger

#         return larger


from typing import List

class Solution:
    def plus(self, num1: List[int], num2: List[int]) -> List[int]:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            s = carry

            if i >= 0:
                s += num1[i]
                i -= 1

            if j >= 0:
                s += num2[j]
                j -= 1

            result.append(s % 10)
            carry = s // 10

        return result[::-1]
        
s = Solution()

def num_to_list(n: int):
    return list(map(int, str(n)))

test_cases = [
    (1, 0),
    (100, 999),
    (958, 2811),
    (999, 999),
]

for x in test_cases:
    a, b = x
    print(s.plus(num_to_list(a), num_to_list(b)))