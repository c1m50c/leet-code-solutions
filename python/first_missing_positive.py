# https://leetcode.com/problems/first-missing-positive/ #
from typing import *


class Solution:
    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        nums_max: int = max(nums)
        nums = set(nums) # For O(1) Lookup Times with `in` operator

        for i in range(1, nums_max + 2):
            if not i in nums:
                return i
        return 1