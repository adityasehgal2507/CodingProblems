'''
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/


|Symbol	|Value  |
| ----- | ----- |
| I	    | 1     |
| V	    | 5     |
| X	    | 10    |
| L	    | 50    |
| C	    | 100   |
| D	    | 500   |
| M	    | 1000  |

1994 = M + CM + XC + IV
1854 = M + DCCC + L + IV
        1000 + (500 + 3*100) + 50 + (5-1)
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        sol = ""
        one = {0: 'I', 1: 'X', 2: 'C', 3: 'M', 4: 'X\''}
        five = {0: 'V', 1: 'L', 2: 'D', 3: 'V\''}
        size = len(str(num))
        for i, digit in enumerate([int(x) for x in str(num)]):
            place = size - i - 1

            if (digit == 4):
                sol += (one[place]) + (five[place])
            elif (digit == 9):
                sol += one[place] + one[place+1]
            elif (digit < 4):
                sol += one[place] * digit
            elif (digit >= 5 and digit < 9):
                sol += (five[place]) + (one[place] * (digit - 5))

        return sol

print(Solution().intToRoman(15854))