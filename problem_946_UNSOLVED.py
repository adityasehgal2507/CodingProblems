'''
Given two integer arrays pushed and popped each with distinct values, 
    return true if this could have been the result of a sequence of push and pop operations 
        on an initially empty stack, 
    or false otherwise.
'''
from typing import *

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False

        last = pushed.index(popped[0])
        for x in popped:
            if pushed.index(x) - last > 1:
                return False
            last = pushed.index(x)
        return True

print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))