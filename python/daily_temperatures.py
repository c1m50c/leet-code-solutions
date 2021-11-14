# https://leetcode.com/problems/daily-temperatures/ #
from typing import *


class Solution:
    @staticmethod
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        n: int = len(temperatures)
        result: List[int] = [0] * n
        h: int = 0
        
        for i in range(n - 1, -1, -1):
            current: int = temperatures[i]
            
            if current >= h:
                h = current
                continue
            
            gap: int = 1
            while temperatures[i + gap] <= current:
                gap += result[i + gap]
            result[i] = gap
        
        return result