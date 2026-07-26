class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap,(freq, num))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap,(freq, num))
        topK = [num for freq, num in heap]
        return topK
        