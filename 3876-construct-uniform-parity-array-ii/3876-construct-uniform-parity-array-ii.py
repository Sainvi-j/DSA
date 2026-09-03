class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)

        if mn % 2 == 1:
            return True
        else:
            for num in nums1:
                if num % 2 == 1:
                    return False
        
        return True