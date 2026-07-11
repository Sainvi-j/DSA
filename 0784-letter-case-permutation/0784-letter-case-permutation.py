class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        op = [""]

        for c in s:
            temp = []
            if c.isalpha():
                for o in op:
                    temp.append(o+c.lower())
                    temp.append(o+c.upper())
            else:
                for o in op:
                    temp.append(o+c)
            op = temp
        return op
