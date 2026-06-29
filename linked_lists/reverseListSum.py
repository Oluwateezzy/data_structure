# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode()
        current_node = result_head
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 0
            current_node.next = ListNode(total % 10)
            current_node = current_node.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry > 0:
            current_node.next = ListNode(carry)
        return result_head.next