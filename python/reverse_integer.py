# https://leetcode.com/problems/reverse-integer/ #
from typing import *


class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        
        if x[0] == "-":
            x = x.removeprefix("-")
            x = int("-" + x[::-1])
        else:
            x = int(x[::-1])
        
        if x > 2147483648:
            return 0
        elif x < -2147483648:
            return 0
        
        return x