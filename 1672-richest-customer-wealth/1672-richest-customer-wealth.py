class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        rich = 0
        for i in accounts:
            rich = max(rich, sum(i))
        return rich