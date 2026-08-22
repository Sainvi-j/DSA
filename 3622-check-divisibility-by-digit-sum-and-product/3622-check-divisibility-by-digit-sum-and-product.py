class Solution:
    def checkDivisibility(self, n: int) -> bool:
        Dsum = 0
        Dprod = 1
        og = n

        while n>0:
            Dg = n%10
            n //= 10

            Dsum += Dg
            Dprod *= Dg
        
        return og % (Dsum + Dprod) == 0