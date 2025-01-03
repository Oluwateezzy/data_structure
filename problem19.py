"""
 You are given an array apple of size n and an array capacity of size m.

There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.

Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.

Note that, apples from the same pack can be distributed into different boxes.


"""

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        sorted_capacity = sorted(capacity, reverse=True)
        current_capacity = 0

        for i in range(len(sorted_capacity)):
            current_capacity += sorted_capacity[i]
            if current_capacity >= total_apples:
                return i + 1

        
        return -1
