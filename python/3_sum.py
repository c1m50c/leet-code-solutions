# https://leetcode.com/problems/3sum/ #
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        result: Set = set()
        
        nums.sort()
        for i in range(0, n):
            j, k = i + 1, n - 1
            while j < k:
                s: int = nums[i] + nums[j] + nums[k]
                
                if not s:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif s > 0: k -= 1
                else: j += 1
        
        return [list(x) for x in result]