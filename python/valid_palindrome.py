# https://leetcode.com/problems/valid-palindrome/ #
from typing import *
import re


class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        # Strip String of non-alphanumerics and covert it to lowercase
        s = "".join(re.split('[^a-zA-Z0-9]+', s)).lower()
        return s == s[::-1]