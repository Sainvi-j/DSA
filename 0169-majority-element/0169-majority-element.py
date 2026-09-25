class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        ele = 0

        for num in nums:
            if count == 0:
                ele = num
            
            if num == ele:
                count += 1
            else:
                count -= 1
        return ele