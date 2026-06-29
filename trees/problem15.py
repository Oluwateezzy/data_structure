"""
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.inorder(root1)
        self.inorder(root2)

        return sorted(self.arr)
    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            self.arr.append(root.val)
            self.inorder(root.right)
        