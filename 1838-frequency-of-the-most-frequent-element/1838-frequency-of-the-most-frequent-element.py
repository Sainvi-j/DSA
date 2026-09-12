class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n= len(nums)
        l=0
        wSum = 0
        best = 1

        for r in range(n):
            wSum += nums[r]

            while nums[r] * (r-l+1) - wSum > k:
                wSum -= nums[l]
                l += 1
            
            best = max(best, r - l + 1)
        
        return best