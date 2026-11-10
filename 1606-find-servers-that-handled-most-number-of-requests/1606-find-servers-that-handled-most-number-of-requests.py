class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        heap = []
        server = [0] * k
        free = SortedList(range(k))
        for i in range(len(arrival)):
            arr, l = arrival[i], load[i]
            while heap and heap[0][0] <= arr:
                _, s_idx = heapq.heappop(heap)
                free.add(s_idx)
            if not free: 
                continue
            idx = free.bisect_left(i%k)
            if idx == len(free): 
                idx = 0
            s = free.pop(idx)
            heapq.heappush(heap, (arr+l, s))
            server[s] += 1
        
        max_ = max(server)
        res = []
        for i, time in enumerate(server):
            if time == max_:
                res.append(i)
        return res