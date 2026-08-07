
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        for i in range(2, 10):
            while temp % i == 0:
                temp //= i
        
        if temp > 1:
            return '-1'

        n = len(num)
        rem = [0] * (n+1)
        rem[0] = t
        pos = n-1

        numList = list(num)

        for i in range(n):
            if numList[i] == '0':
                pos = i
                break
            rem[i+1] = rem[i] // math.gcd(rem[i], int(numList[i]))
        
        if rem[n] == 1:
            return num
        
        for i in range(pos, -1, -1):
            while True:
                numList[i] = chr(ord(numList[i]) + 1)
                if numList[i] > '9':
                    break
                
                t_curr = rem[i] // math.gcd(rem[i], int(numList[i]))

                k = 9

                for j in range(n-1, i, -1):
                    while t_curr % k != 0:
                        k -= 1
                    
                    t_curr //= k
                    numList[j] = str(k)
                
                if t_curr == 1:
                    return "".join(numList)
        ans = []
        ogt = t

        for i in range(9, 1, -1):
            while ogt % i == 0:
                ans.append(str(i))
                ogt //= i

        ansstr = "".join(ans)
        pad = max(n+1 - len(ansstr), 0)
        ansstr += "1" * pad

        return ansstr[::-1]   