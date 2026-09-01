from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litterPos = []
        start = None
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start = (r, c)
                elif ch == 'L':
                    litterPos.append((r, c))

        k = len(litterPos)
        litterIndex = {pos: i for i, pos in enumerate(litterPos)}
        fullMask = (1 << k) - 1 if k > 0 else 0

        if k == 0:
            return 0

        sr, sc = start
        initMask = 0
        if (sr, sc) in litterIndex:
            initMask |= (1 << litterIndex[(sr, sc)])

        visited = set()
        startState = (sr, sc, energy, initMask)
        visited.add(startState)
        queue = deque([startState])
        moves = 0

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            for _ in range(len(queue)):
                r, c, e, mask = queue.popleft()
                if mask == fullMask:
                    return moves
                if e == 0:
                    continue
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if classroom[nr][nc] == 'X':
                        continue
                    newEnergy = e - 1
                    newMask = mask
                    if classroom[nr][nc] == 'R':
                        newEnergy = energy
                    if (nr, nc) in litterIndex:
                        newMask = mask | (1 << litterIndex[(nr, nc)])
                    state = (nr, nc, newEnergy, newMask)
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)
            moves += 1

        return -1