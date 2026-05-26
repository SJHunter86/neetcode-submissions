class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in counts.items():
            freq[value].append(key)
        
        result = []
        for i in range(len(freq) - 1, -1, -1):
            result.extend(freq[i])
            if len(result) >= k:
                return result[:k]
        return None