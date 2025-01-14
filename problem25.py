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


## Time Complexity: O(log(n))
## Space Complexity: O(1)

## Pythonic solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    
## Time Complexity: O(1)
## Space Complexity: O(1)

# The pythonic solution is better than the first solution because it is more readable and concise. It uses the built-in function bin() to convert the integer to binary and then uses the count() method to count the number of set bits. This solution is more efficient and easier to understand than manually counting the set bits.

# The time complexity of the first solution is O(log(n)) because we are dividing the number by 2 in each iteration until it becomes 0. The space complexity is O(1) because we are using a constant amount of space to store the count.

## Brian Kernighan’s Algorithm
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

## Time Complexity: O(log(n))
## Space Complexity: O(1)

# The Brian Kernighan’s Algorithm is an optimized solution that uses bitwise operations to count the number of set bits. It works by repeatedly flipping the least significant set bit to 0 until the number becomes 0. This algorithm has a time complexity of O(log(n)) and a space complexity of O(1), making it more efficient than the first solution.

## Bitwise AND
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

## Time Complexity: O(log(n))
## Space Complexity: O(1)

# The Bitwise AND solution is similar to the first solution but uses bitwise AND to check the least significant bit instead of modulo. This solution has a time complexity of O(log(n)) and a space complexity of O(1), making it less efficient than the Brian Kernighan’s Algorithm but still better than the first solution.

print(11 & 1)
print(11 >> 1)
print(5 & 1)


## >> is the right shift operator which shifts the bits of a number to the right by a specified number of positions. For example, 11 >> 1 shifts the bits of 11 to the right by 1 position, resulting in 5. The & operator performs a bitwise AND operation between two numbers, returning 1 if both bits are 1 and 0 otherwise. For example, 11 & 1 returns 1 because the least significant bit of 11 is 1.
