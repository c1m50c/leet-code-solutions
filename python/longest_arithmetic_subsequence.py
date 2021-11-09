from collections import defaultdict
from typing import *


# Section for LeetCode
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n: int = len(nums)
        result: int = 2
        
        dp = [defaultdict(int) for _ in range(0, n)]
        
        for i in range(1, n):
            for j in range(0, i):
                difference: int = nums[i] - nums[j]
                dp[i][difference] = max(2, dp[j][difference] + 1)
                result = max(result, dp[i][difference])

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestArithSeqLength([9, 4, 7, 2, 10]))