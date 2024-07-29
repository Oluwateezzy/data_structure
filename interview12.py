"""
    Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

    Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
    Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.

"""

import collections
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        nums_dict1 = collections.Counter()
        nums_dict2 = collections.Counter()

        for num in nums1:
            nums_dict1[num * num] += 1
        for num in nums2:
            nums_dict2[num * num] += 1
        
        count = 0

        for j in range(len(nums2)):
            for k in range(j+1, len(nums2)):
                if nums2[j] * nums2[k] in nums_dict1:
                    count += nums_dict1[nums2[j] * nums2[k]]
        
        for j in range(len(nums1)):
            for k in range(j+1, len(nums1)):
                if nums1[j] * nums1[k] in nums_dict2:
                    count += nums_dict2[nums1[j] * nums1[k]]
        

        return count


"""
    Refactored Solution
"""

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count_pairs(nums: List[int], target_dict: collections.Counter) -> int:
            count = 0
            for j in range(len(nums)):
                for k in range(j + 1, len(nums)):
                    product = nums[j] * nums[k]
                    if product in target_dict:
                        count += target_dict[product]
            return count

        nums_dict1 = collections.Counter(num * num for num in nums1)
        nums_dict2 = collections.Counter(num * num for num in nums2)

        count = 0
        count += count_pairs(nums2, nums_dict1)
        count += count_pairs(nums1, nums_dict2)

        return count