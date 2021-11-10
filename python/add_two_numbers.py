# https://leetcode.com/problems/add-two-numbers/ #

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        previous = ListNode()
        current, carry = previous, 0
        
        while l1 != None or l2 != None:
            x, y = 0, 0
            
            if l1: x = l1.val
            if l2: y = l2.val
            
            num_sum = x + y + carry
            carry = num_sum // 10
            num_sum %= 10
            current.next = ListNode(val=num_sum)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry != 0: current.next = ListNode(val=carry)
        return previous.next