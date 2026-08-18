'''

The Reverse Challenge: "Preimage Size of Factorial Zeroes"
The Problem: You are given an integer k. 
How many non-negative integers 'n' have exactly 'k' trailing zeroes in 'n!'?

a = 0, 
b = Min Number with n trailing 0s
Number of trailing 0s = Number of 5s in n!
Number of 5s in n! > 5*k

BUT factors of 5 in n! is Legendre's Formula
Sum from 1 to inf of (n//5^i)
Substituting Base-5 into Legendre's Formula
-> k = Sum a_m * (5^m-1) / 4
a_m can only be 0, 1, 2, 3 or 4, If a_m = 5, then forbidden

class Solution:
    # O(log_5(k)) ~ O(ln(k)/1.60943791243)
    def preimageSizeFZF(self, k: int) -> int:
        # Generate Legendre weights: [1, 6, 31, 156, ...]
        weights = []
        w = 1
        while w <= k:
            weights.append(w)
            w = w * 5 + 1
            
        # Walk backwards from largest weight to smallest
        for w in reversed(weights):
            if k // w == 5: 
                return 0  # Invalid digit found!
            k %= w
            
        return 5

n = 12 -> 1*5, 2*5 -> 2 trailing
n = 25 -> 1*5, 2*5, 3*5, 4*5, 5*5 -> 6 trailing
=> Upper bound = 5k

'''

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # Helper function from the first problem to count trailing zeroes
        def countZeroes(n: int) -> int:
            count = 0
            while n >= 5:
                n //= 5
                count += n
            return count

        # Binary search to find if any number produces exactly k zeroes
        low = 0
        high = 5 * k + 1  # Safe upper bound
        
        while low <= high:
            mid = (low + high) // 2
            current_zeroes = countZeroes(mid)
            
            if current_zeroes == k:
                return 5  # If one number works, its 5-number block all work!
            elif current_zeroes < k:
                low = mid + 1
            else:
                high = mid - 1
                
        return 0  # k was skipped because of a 'secret' extra 5

def to_base_5(n):
    if n == 0:
        return "0"
    
    digits = []
    while n > 0:
        n, remainder = divmod(n, 5)
        digits.append(str(remainder))
        
    return "".join(reversed(digits))

for i in range(1, 31):
    ans = Solution().preimageSizeFZF(i)
    if ans == 0:
        print(f"{to_base_5(i)}={0}")