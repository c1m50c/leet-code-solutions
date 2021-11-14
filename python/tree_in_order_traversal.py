# https://leetcode.com/problems/binary-tree-inorder-traversal/ #
from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        queue: List[TreeNode] = [  ]
        current: TreeNode = root
        result: List[int] = [  ]
        
        while True:
            if current:
                queue.append(current)
                current = current.left
            elif queue:
                current = queue.pop()
                result.append(current.val)
                current = current.right
            else:
                break

        return result