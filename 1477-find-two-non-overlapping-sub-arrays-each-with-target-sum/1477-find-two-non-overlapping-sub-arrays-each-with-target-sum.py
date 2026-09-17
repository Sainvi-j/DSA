class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        l, wd, res = 0, 0, float('inf')
        minTill = [float('inf')] * len(arr)

        for r, num in enumerate(arr):
            wd += num

            while wd > target:
                wd -= arr[l]
                l += 1
            
            if wd == target:
                curLen = r - l + 1
                res = min(res, curLen+minTill[l-1])
                minTill[r] = min(curLen, minTill[r-1])
            
            else:
                minTill[r] = minTill[r-1]
        return res if res < float('inf') else -1
