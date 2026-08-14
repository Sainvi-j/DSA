class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        return max(j-i for i,j in combinations(range(len(s)+1),2)
            if max(Counter(s[i:j]).values())<3)
