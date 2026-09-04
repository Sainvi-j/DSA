class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            cur = max(nums[:i+1]) - min(nums[i:])
            if cur <= k:
                return i
        return -1