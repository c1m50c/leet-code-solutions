# https://leetcode.com/problems/letter-combinations-of-a-phone-number/ #
from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return [  ]
        key_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        result: List[str] = key_letters[digits[0]]
        for c in digits[1:]:
            temp: List[str] = [  ]
            for i in result:
                for j in key_letters[c]:
                    temp.append(i + j)
            result = temp
        
        return result