class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        valid = set()
        
        for d1, d2, d3 in permutations(digits, 3):
            if d1 == 0:
                continue

            if d3 % 2 != 0:
                continue
        
            valid.add(d1 * 100 + d2 * 10 + d3)
        return len(valid)
        
