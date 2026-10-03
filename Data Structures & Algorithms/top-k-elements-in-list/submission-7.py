class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min heap so root is the smallest value
        min_heap = []
        freqs = Counter(nums)

        for key, v in freqs.items():
            heapq.heappush(min_heap, (v, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [v for _, v in min_heap]