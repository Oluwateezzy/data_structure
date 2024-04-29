"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
"""

from typing import List


def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        n = len(citations)
        for i, v in enumerate(citations):
            if n - i <= v:
                return n -i
        return 0