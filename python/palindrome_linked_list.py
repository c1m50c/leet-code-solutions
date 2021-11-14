# https://leetcode.com/problems/palindrome-linked-list/ #
from typing import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def isPalindrome(head: Optional[ListNode]) -> bool:
        s: str = ""
        
        while head:
            s += str(head.val)
            head = head.next
        
        return s == s[::-1]