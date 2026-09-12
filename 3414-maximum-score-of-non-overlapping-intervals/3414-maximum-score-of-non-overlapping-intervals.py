class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        od = sorted(range(n), key=lambda i: intervals[i][1])
        st = [intervals[od[i]][0] for i in range(n)]
        end = [intervals[od[i]][1] for i in range(n)]
        wt = [intervals[od[i]][2] for i in range(n)]

        prev = [0] * n

        for i in range(n):
            lo, hi, pos = 0, i-1, -1
            while lo <= hi:
                mid = (lo+hi) // 2
                if end[mid] < st[i]:
                    pos = mid
                    lo = mid+1
                else:
                    hi = mid-1
            prev[i] = pos+1

        dp = [[(0,[]) for _ in range(5)] for _ in range(n+1)]

        def better(a,b):
            if a[0] != b[0]:
                return a[0]> b[0]
            return a[1]< b[1]

        for i in range(1, n+1):
            cur = od[i-1]
            w = wt[i-1]
            for k in range(5):
                best= dp[i-1][k]
                if k >= 1:
                    prevSc, prevLst = dp[prev[i-1]][k-1]
                    cnd = (prevSc + w, sorted(prevLst + [cur]))
                    if better(cnd, best):
                        best = cnd
                dp[i][k] = best

        return dp[n][4][1] 
