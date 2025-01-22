from typing import List

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, 
nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    print(nums1.__repr__)
    for i in range(n):
        nums1.pop(m)
        nums1.append(nums2[i])
    

    nums1.sort()
    print(nums1)
    print(nums1.__repr__)

merge([1,2,3,0,0,0], 3, [2,5,6], 3)

# The merge function takes two sorted arrays nums1 and nums2, along with their lengths m and n, and merges them into a single sorted array. The function modifies the nums1 array in-place to store the merged result.