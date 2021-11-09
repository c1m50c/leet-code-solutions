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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_list: List[ListNode] = [  ]
        temp_node: ListNode = head
        
        while temp_node:
            temp_list.append([temp_node.val, temp_node])
            temp_node = temp_node.next
        
        temp_list.sort(key = lambda val : val[0])
        
        if len(temp_list) > 0:
            temp_node = temp_list[0][1]
            temp_node.next = None
            
            for i in temp_list[1:]:
                temp_node.next = i[1]
                temp_node = temp_node.next
            
            temp_node.next = None
            return temp_list[0][1]
        
        return None


if __name__ == "__main__":
    sol = Solution()
    sol.sortList()