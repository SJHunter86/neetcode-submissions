class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        
        heap = []
        for key, v in freqs.items():
            heapq.heappush(heap, (-v, key))
        
        result = []
        while heap and k > 0:
            k -= 1
            key = heapq.heappop(heap)[1]
            result.append(key)
        
        return result