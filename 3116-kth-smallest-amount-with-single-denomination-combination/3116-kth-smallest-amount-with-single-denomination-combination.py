class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        from math import gcd
        
        coins.sort()
        
        if coins[0] == 1:
            return k
        
        n = len(coins)
        r = 0
        
        
        i = 0
        while i < n - r - 1:
            c = coins[i]
            j = i + 1
            
            while j < n - r:
                if coins[j] % c == 0:
                    coins.pop(j)
                    r += 1
                else:
                    j += 1
            
            i += 1
        
        a = n - r
        
        if a == 1:
            return coins[0] * k
        
        coins = coins[:a]
        
        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b
        
        def countNums(m: int) -> int:
            total = 0
            total_masks = 1 << a
            
            for mask in range(1, total_masks):
                common = 1
                bits = 0
                
                for i in range(a):
                    if (mask & (1 << i)) != 0:
                        common = lcm(common, coins[i])
                        bits += 1
                
                if bits & 1 == 1:
                    total += m // common
                else:
                    total -= m // common
            
            return total
        
        
        low = coins[0]
        high = coins[0] * k
        result = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            count = countNums(mid)
            
            if count >= k:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result