class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rsum(a, b):  
            return prefix[b + 1] - prefix[a]

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]  
        maxR = [[0] * n for _ in range(n)]  

        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                total = rsum(i, j)

                lo, hi, mid = i, j - 1, i - 1
                while lo <= hi:
                    m = (lo + hi) // 2
                    s = rsum(i, m)
                    if s * 2 <= total:
                        mid = m
                        lo = m + 1
                    else:
                        hi = m - 1

                best = 0
                if mid >= i:
                    best = max(best, maxL[i][mid])
                if mid + 2 <= j:
                    best = max(best, maxR[mid + 2][j])
                if mid >= i and mid + 1 <= j:
                    ls = rsum(i, mid)
                    rs = rsum(mid + 1, j)
                    if ls == rs:
                        best = max(best, rs + dp[mid + 1][j])

                dp[i][j] = best
                maxL[i][j] = max(maxL[i][j - 1], total + dp[i][j])
                maxR[i][j] = max(maxR[i + 1][j], total + dp[i][j])

        return dp[0][n - 1]