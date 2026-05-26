class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = len(nums)
        freq_dict = defaultdict(int)
        freq_table = [[] for _ in range(max_freq + 1)]
        result = []

        for num in nums:
            freq_dict[num] += 1
        
        for num, freq in freq_dict.items():
            freq_table[freq].append(num)
        
        for i in range(len(freq_table)-1, -1, -1):
            result.extend(freq_table[i])
            if len(result) >= k:
                return result[:k]
        
        return result