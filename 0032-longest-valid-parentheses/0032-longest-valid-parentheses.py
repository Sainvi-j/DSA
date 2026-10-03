class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxLen = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1])
        return maxLen