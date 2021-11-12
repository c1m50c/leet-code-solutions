# https://leetcode.com/problems/longest-palindromic-substring/ #
from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n: int = len(s)
        result: List[str] = [  ]
        if n <= 1: return s

        for i in range(0, n):
            l, r, = i, i # l: Left, r: Right
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(result):
                    result = s[l : r + 1]
                l -= 1
                r += 1

            l, r = i - 1, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(result):
                    result = s[l : r + 1]
                l -= 1
                r += 1

        return result