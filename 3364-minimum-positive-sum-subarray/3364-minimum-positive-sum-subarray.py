class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')

        for size in range(l, r+1):
            total = sum(nums[:size])

            if total > 0:
                min_sum = min(min_sum, total)
            
            for right in range(size, len(nums)):
                total = total + nums[right] - nums[right-size]

                if total > 0:
                    min_sum = min(min_sum, total)
            
        
        if min_sum == float('inf'):
            return -1
        else:
            return min_sum