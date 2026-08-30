class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        sortedEnum = sorted((num,i) for i, num in enumerate(nums))

        newPos = []
        currPos = []
        prev = float('-inf')

        for num, idx in sortedEnum:
            if num > prev + limit:
                newPos.extend(sorted(currPos))
                currPos = [idx]
            else:
                currPos.append(idx)
            prev = num
        
        newPos.extend(sorted(currPos))

        res = [0] * n

        for i, idx in enumerate(newPos):
            res[idx] = sortedEnum[i][0]
        
        return res