class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums = sorted(nums)
        count = 0
        for i in range(len(nums) - 1, 0, -1):
            count += nums[i] - nums[0]
        return count