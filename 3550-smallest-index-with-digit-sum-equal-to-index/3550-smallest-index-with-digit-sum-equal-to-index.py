class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = nums[i]
            a = 0
            while x > 0:
                a += x % 10
                x //= 10
            if a == i:
                return i
        return -1
