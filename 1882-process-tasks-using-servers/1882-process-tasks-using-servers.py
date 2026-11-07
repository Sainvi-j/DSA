class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n, m = len(servers), len(tasks)
        ans = []
        heapsmol = []
        heaplarge = []

        for idx, weight in enumerate(servers):
            heappush(heapsmol, (weight, idx, 0))

        for i, task in enumerate(tasks):
            while heaplarge and heaplarge[0][0] <= i:
                time, weight, index = heappop(heaplarge) 
                heappush(heapsmol, (weight, index, time))
            
            if heapsmol:
                weight, index, time = heappop(heapsmol)
                ans.append(index)
                heappush(heaplarge, (i + task, weight, index))
            else:
                time, weight, index = heappop(heaplarge)
                ans.append(index)
                heappush(heaplarge, (time + task, weight, index))
        
        return ans