class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2

        l = num[:half]
        r = num[half:]

        q1 = l.count("?")
        q2 = r.count("?")

        if (q1 + q2) % 2 != 0:
            return True

        s1 = sum(map(int, l.replace("?", "0")))
        s2 = sum(map(int, r.replace("?", "0")))

        return (2 * s1 + 9 * q1) != (2 * s2 + 9 * q2)