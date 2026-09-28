class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        op = 0

        for c in s:
            if c == "(":
                op += 1
            elif c == ")":
                op -= 1
            
            ans = max(ans, op)
        return ans