'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing each maximal group of consecutive identical characters with the concatenation of the length of the group followed by the character itself. For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15", and replace "1" with "11". Thus the compressed string becomes "23321511".
Given a positive integer n, return the nth element of the count-and-say sequence.
'''

import re

def getFreq(text):
    matches = "".join([f"{len(m.group(0))}{m.group(0)[0]}"
                for m in re.finditer(r"(.)\1*", text)])
    return matches

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return getFreq(self.countAndSay(n - 1))

print(Solution().countAndSay(4))