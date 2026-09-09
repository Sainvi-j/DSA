class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 999:
            return 0

        TC = 0
        st = 1000

        while st <= n:
            TC += n - st + 1
            st *= 1000
        
        return TC