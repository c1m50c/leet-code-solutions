from __future__ import annotations
from typing import *


class ListNode:
    val: any
    next: ListNode
    
    def __init__(self, val: any = 0, next: ListNode = None) -> None:
        self.val = val
        self.next = next


# Section for LeetCode
class Solution:
    @staticmethod
    def insert_sorted(head: ListNode, new: ListNode) -> None:
        current: ListNode = None
        
        if not head or head.val >= new.val:
            new.next = head
            head = new
        else:
            current = head
            while current.next and current.next.val < new.val:
                current = current.next
            new.next = current.next
            current.next = new
        
        return head
    
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Insertion Sort for a Singly Linked List
            ```py
            Worst Case Time Complexity == O(n * n)
            Average Case Time Complexity == O(n * n)
            Best Case Time Complexity == O(n)
            ```
        """
        
        current, sorted_node = head, None
        
        while current:
            next = current.next
            sorted_node = Solution.insert_sorted(sorted_node, current)
            current = next
        return sorted_node


if __name__ == "__main__":
    sol = Solution()
    sol.sortList()