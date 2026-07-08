class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r-l+1)

                total -= nums[l]
                l+=1
        
        if res == float('inf'):
            return 0
        else:
            return res

        