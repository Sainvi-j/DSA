class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1
        if target == 0:
            return n

        l = 0
        s = 0
        longg = -1

        for r in range(n):
            s += nums[r]

            while l <= r and s > target:
                s -= nums[l]
                l += 1
            
            if s == target:
                longg = max(longg, r - l + 1)
        
        return -1 if longg == -1 else n - longg