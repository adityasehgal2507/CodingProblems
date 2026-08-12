'''
Roman to Integer
'''

from typing import *

values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        prev = None
        for x in s[::-1]:
            if prev and values[prev] > values[x]:
                val -= values[x]
            else:
                val += values[x]
            prev = x
        return val

def test_solution(func, tests):
    for i, (args, expected) in enumerate(tests, 1):
        result = func(*args)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"  Input:    {args}\n"
            f"  Expected: {expected}\n"
            f"  Got:      {result}"
        )

    print(f"All {len(tests)} tests passed!")

if __name__ == "__main__":
    tests = [
        (("III",), 3),
        (("IV",), 4),
        (("IX",), 9),
        (("LVIII",), 58),
        (("MCMXCIV",), 1994),
        (("I",), 1),
        (("V",), 5),
        (("X",), 10),
        (("L",), 50),
        (("C",), 100),
        (("D",), 500),
        (("M",), 1000),
        (("VIII",), 8),
        (("XIII",), 13),
        (("XL",), 40),
        (("XC",), 90),
        (("CD",), 400),
        (("CM",), 900),
        (("XLII",), 42),
        (("MMXXIV",), 2024),
    ]

    test_solution(Solution().romanToInt, tests)