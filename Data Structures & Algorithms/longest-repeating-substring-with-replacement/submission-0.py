class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        n = len(s)
        longest = 1
        left = 0

        for right in range(n):
            counts[s[right]] += 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        
        return longest

"""
AAABABB - k = 1
counts {
    A: 1
    B: 0
}
left 0, right 0, count 0

"""