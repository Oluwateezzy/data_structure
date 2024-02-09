from typing import List

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        unique = set(nums)
        for i in unique:
            if nums.count(i) > mid:
                return i


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        mid = len(nums) // 2
    
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > mid:
                return num