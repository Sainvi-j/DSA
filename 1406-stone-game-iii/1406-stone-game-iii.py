class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = [None] * (n + 1)

        def diff(i):
            if i >= n:
                return 0
            if memo[i] is not None:
                return memo[i]

            best = float("-inf")
            runningSum = 0
            for k in range(1, 4):
                if i + k - 1 >= n:
                    break
                runningSum += stoneValue[i + k - 1]
                candi = runningSum - diff(i + k)
                best = max(best, candi)

            memo[i] = best
            return best

        result = diff(0)
        if result > 0:
            return "Alice"
        elif result < 0:
            return "Bob"
        else:
            return "Tie"