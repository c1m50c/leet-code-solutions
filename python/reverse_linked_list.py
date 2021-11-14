# https://leetcode.com/problems/reverse-linked-list/ #
from typing import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
           return None

        new: ListNode = head
        if head.next:
            new = Solution.reverseList(head.next)
            head.next.next = head
        
        head.next = None
        return new