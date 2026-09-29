class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 == 1 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        @cache
        def dfs(i: int, j: int, k: int) -> bool:
            k += 1 if grid[i][j] == '(' else -1
            
            if k < 0 or k > m - i + n - j - 1:
                return False

            if i == m - 1 and j == n - 1:
                return k == 0
                
            res = False
            if i + 1 < m:
                res = res or dfs(i + 1, j, k)
            if not res and j + 1 < n:
                res = res or dfs(i, j + 1, k)
                
            return res

        return dfs(0, 0, 0)