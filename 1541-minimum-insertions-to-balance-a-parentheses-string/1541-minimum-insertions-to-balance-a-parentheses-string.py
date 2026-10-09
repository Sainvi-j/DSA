class Solution:
    def minInsertions(self, s: str) -> int:
        res = temp = 0
        need = False

        for ch in s:
            if ch == '(':
                if need:
                    res += 1
                    need = False
                temp += 1
            else:
                if need:
                    need = False
                else:
                    if temp == 0:
                        temp += 1
                        res += 1
                    temp -= 1
                    need = True
        if need:
            res += 1
        res += temp * 2
        return res