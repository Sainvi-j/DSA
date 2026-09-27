class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)

        left, right = 0, n-1
        for _ in range(n):
            sm = numbers[left] + numbers[right]

            if sm == target:
                return [left + 1, right + 1]
            
            if sm < target:
                left += 1
            else:
                right -= 1