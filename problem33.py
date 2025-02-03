"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1] * i for i in range(1, numRows + 1)]
        for i in range(2, len(arr)):
            for j in range(1, len(arr[i]) - 1):
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
        return arr
