class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        freq_table = [[] for _ in range(len(nums) + 1)]
        for key, value in freq_map.items():
            freq_table[value].append(key)
        
        result = []
        for i in range(len(freq_table) - 1, -1, -1):
            if freq_table[i]:
                while freq_table[i]:
                    result.append(freq_table[i].pop())
                    if len(result) == k:
                        return result
        return None