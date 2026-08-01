from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache
        def diff(i, j):
            if i == j:
                return nums[i]
            takeLeft = nums[i] - diff(i+1, j)
            takeRight = nums[j] - diff(i, j-1)

            return max(takeLeft, takeRight)
        return diff(0, n-1) >= 0
