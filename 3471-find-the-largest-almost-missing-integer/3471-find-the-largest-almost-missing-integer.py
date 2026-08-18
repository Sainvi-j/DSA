class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = {}

        for st in range(0, n-k+1):
            wd = nums[st: st+k]
            distVal = set(wd)

            for v in distVal:
                cnt[v] = cnt.get(v,0)+1

        ans = -1
        for v in cnt:
            if cnt[v] == 1:
                ans = max(ans, v) 
        
        return ans