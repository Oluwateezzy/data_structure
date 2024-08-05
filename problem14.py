"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.
"""

# greedy solution
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #ababccc
        temp = ''
        arr = []

        for letter in s:
            temp += letter
            if temp not in arr:
                arr.append(temp)
                temp = ''

        return len(arr)

