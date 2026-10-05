class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.time_map[key]
        lo, hi = 0, len(data)-1
        result = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            if data[mid][0] == timestamp:
                return data[mid][1]
            elif data[mid][0] < timestamp:
                result = data[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return result

"""
- can't use just key because there's duplicates
- if not found, last known val, so lo or hi index 1
- set must be O(1)
- get must be O(log n) <- binary search?
- space must be O(m * n)

{
    "alice": [(1, "happy"), (3, "sad")]
}
"""