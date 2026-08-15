class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        totalxor = 0
        isNonzero = False

        for num in nums:
            totalxor = totalxor ^ num
            if num != 0:
                isNonzero = True
        
        n = len(nums)

        if totalxor != 0:
            return n
        else:
            if isNonzero:
                return n-1
            else:
                return 0