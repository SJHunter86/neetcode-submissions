class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums) + 1
        freq_dict = defaultdict(int)
        freq_table = [[] for _ in range(length)]
        for num in nums:
            freq_dict[num] += 1
        
        for key, value in freq_dict.items():
            freq_table[value].append(key)
        
        result = []
        for i in range(length-1, -1, -1):
            while len(freq_table[i]):
                result.append(freq_table[i].pop())
                if len(result) == k:
                    return result