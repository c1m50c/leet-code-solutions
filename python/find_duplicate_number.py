# https://leetcode.com/problems/find-the-duplicate-number/ #
from typing import *


class Solution:
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        i, n = 0, len(nums)
        
        while i < n:
            idx: int = nums[i] - 1
            
            if nums[i] != nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i] # Swap
            else:
                i += 1
        
        for j in range(0, n):
            if nums[j] != j + 1:
                return nums[j]
        return -1