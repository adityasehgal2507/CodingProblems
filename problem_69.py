import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        a, b = 1, x
        c = (a + b) // 2
        while b-a > 1:
            if (c+1)*(c+1) > x > c*c:
                return c
            elif c*c > x:
                b = c
            else:
                a = c
            c = (a + b) // 2
        return c

s = Solution()
for x in range(1, 21):
    print(s.mySqrt(x) == int(math.sqrt(x)))
