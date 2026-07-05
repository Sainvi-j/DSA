class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_list = [num ** 2 for num in nums]
        sq_list.sort()
        return sq_list