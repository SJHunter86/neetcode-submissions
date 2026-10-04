class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(rate):
            time_used = 0
            for pile in piles:
                time_used += (pile + rate - 1) // rate
            return time_used
        min_rate = max(piles)
        lo, hi = 1, min_rate
        
        while lo <= hi:
            k = (lo+hi) // 2
            hours_used = can_finish(k)
            # if hours_used < h, can we go smaller?
            if hours_used <= h:
                min_rate = k
                hi = k - 1
            elif hours_used > h:
                lo = k + 1
        
        return min_rate


"""
[1,4,3,2], h = 9, output is 2

- piles[i] is how many bananas are in that index's pile
- h is the number of hours to eat every pile
- k is how many bananas per hour koko can eat
- every hour, choose a pile of bananas
    - if it has less than k bananas, pile is 0 but the hour is used
- return the minimum value of k that will consume every banana in h hours


- zeroing in on an optimal rate -- start with a range and sharpen it with binary search?
- divide and conquer
- the min is 1, the max amount you can eat is max(piles)
- k is the midpoint

[1,4,3,2] - range is 1..4, (4+1) // 2 = 2
[1,2,2,1] - finish in 6 hours - success
    - looking for min, so if h is still > 0 after finishing, shrink the range
[1,4,3,2] - range is 1..1
[1,4,3,2] - finish in 10 hours, 10 > 9, fail, range is done, return optimal rate
"""