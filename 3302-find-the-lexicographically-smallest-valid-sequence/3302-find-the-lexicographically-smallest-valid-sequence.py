class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        lt = [-1] * m

        i = n-1
        j = m-1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                lt[j] = i
                j -= 1
            i -= 1
            
        ans = []
        skip = True
        j = 0

        for i in range(n):
            if j == m:
                break
            
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            
            elif skip and (j == m-1 or i < lt[j+1]):
                skip = False
                ans.append(i)
                j += 1
        
        if j == m:
            return ans
        
        return []

        