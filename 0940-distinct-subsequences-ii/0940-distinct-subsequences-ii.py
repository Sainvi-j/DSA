class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = 26 * [0]
        mod = (10**9 + 7)
        for i in s:
            idx = ord(i) - ord('a')
            dp[idx] = (sum(dp)+1) % mod
        return sum(dp) % mod