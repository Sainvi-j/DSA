class Solution:
    def func(self, u, adj, vis):
        vis[u] = True

        for v in adj[u]:
            if vis[v]:
                continue
            self.func(v, adj, vis)
    
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[]for _ in range(n)]

        for u, v in invocations:
            adj[u].append(v)
        
        vis = [False] * n
        self.func(k, adj, vis)

        for u, v in invocations:
            if vis[u]:
                continue
            
            if vis[v]:
                return [i for i in range(n)]
        
        ans = []

        for i in range(n):
            if not vis[i]:
                ans.append(i)
        return ans
