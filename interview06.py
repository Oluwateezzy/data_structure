"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        nums[:] = nums[-k:] + nums[:-k]