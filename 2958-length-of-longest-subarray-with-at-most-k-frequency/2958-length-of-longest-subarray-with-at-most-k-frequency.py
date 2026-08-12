class Solution:
    def maxSubarrayLength(self, nums, k):
        m = {}

        i = 0
        res = 0

        for j in range(len(nums)):
            m[nums[j]] = m.get(nums[j], 0) + 1

            while m[nums[j]] > k:
                m[nums[i]] -= 1
                i += 1

            res = max(res, j - i + 1)

        return res