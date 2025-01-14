"""
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n // 2 != 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count + 1

