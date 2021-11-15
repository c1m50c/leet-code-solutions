# https://leetcode.com/problems/valid-parentheses/ #
from typing import *


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack: List[str] = [  ]
        pairs: Dict[str, str] = {
            "{":"}",
            "[":"]",
            "(":")",
        }

        for i in range(0, len(s)):
            if s[i] in pairs.keys():
                stack.append(pairs[s[i]])
            elif s[i] in pairs.values():
                if not stack:
                    return False
                elif s[i] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0