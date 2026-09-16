class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9+7
        dp = [[0] * (k+1) for _ in range(n)]

        for i in range(n):
            dp[i][0]=1

        for j in range(1, k+1):
            tt=0
            for i in range(1,n):
                tt= (tt + dp[i-1][j-1]) % mod
                dp[i][j] = (dp[i-1][j] + tt) % mod
        return dp[n-1][k]