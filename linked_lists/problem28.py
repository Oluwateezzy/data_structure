"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from reverseListSum import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1:
            num1 = num1 + str(l1.val)
            l1 = l1.next
        print(num1)

        while l2:
            num2 = num2 + str(l2.val)
            l2 = l2.next
        total = int(num1[::-1]) + int(num2[::-1])
        print(total)

        head = ListNode()
        current = head

        for i in str(total)[::-1]:
            current.next = ListNode(int(i))
            current = current.next

        return head.next
