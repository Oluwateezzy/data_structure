"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0
        queue = [(root, 0)]

        while queue:
            level_length = len(queue)
            first_index = queue[0][1]

            for i in range(level_length):
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2 * (index - first_index)))
                if node.right:
                    queue.append((node.right, 2 * (index - first_index) + 1))

                if i == level_length - 1:
                    last_index = index
            current_width = last_index - first_index + 1
            max_width = max(max_width, current_width)
        return max_width
