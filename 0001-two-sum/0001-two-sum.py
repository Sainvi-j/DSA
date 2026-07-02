class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for indx, val in enumerate(nums):
            diff = target - val
            if diff in hash_map:
                return(indx, hash_map[diff])
            hash_map[val] = indx