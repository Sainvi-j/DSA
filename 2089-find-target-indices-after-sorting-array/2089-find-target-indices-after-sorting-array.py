class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        idx = []
        for i in range(len(nums)):
            if nums[i] == target:
                idx.append(i)
        return idx
