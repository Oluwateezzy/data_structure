"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= end:
                end = i
        return end == 0   
"""

from typing import List

# solution from neetcode

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= end:
                end = i
        return True if end == 0 else False
    
# My brute-force solution

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        end = len(nums) - 1

        for i in range(len(nums)):
            if nums[i] == 0 and i < end:  # If nums[i] is zero and not already at the end
                return False
            for j in range(1, nums[i] + 1):
                if i + j >= end:
                    return True
        return False