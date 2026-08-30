class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minidx = nums.index(min(nums))
        maxidx = nums.index(max(nums))

        left = min(minidx, maxidx)
        right = max(minidx, maxidx)

        c1 = right + 1
        c2 = n - left
        c3 = (left + 1) + (n - right)

        return min(c1, c2, c3)