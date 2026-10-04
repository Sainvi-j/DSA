class Solution:
    def checkValidString(self, s: str) -> bool:
        openCnt = 0
        closeCnt = 0
        length = len(s) - 1

        for i in range(length + 1):
            if s[i] == '(' or s[i] == "*":
                openCnt += 1
            else:
                openCnt -= 1
            
            if s[length - i] == ')' or s[length - i] == "*":
                closeCnt += 1
            else:
                closeCnt -= 1
            
            if openCnt < 0 or closeCnt < 0:
                return False

        return True