class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = [0]

        for ch in s:
            if ch =='(':
                res.append(0)
            else:
                val = max(2 * res.pop(), 1)
                res[-1] += val
        return res.pop()