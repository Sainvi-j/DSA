class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w, labels[u] == labels[v]))

        done = [k + 1] * n  
        heap = [(0, 0, 1)]
        last = n - 1

        while heap:
            d, u, r = heappop(heap)
            if r >= done[u]: 
                continue
            done[u] = r
            if u == last:
                return d
            for v, w, same in graph[u]:
                nr = r + 1 if same else 1
                if nr < done[v]: 
                    heappush(heap, (d + w, v, nr))

        return -1
        