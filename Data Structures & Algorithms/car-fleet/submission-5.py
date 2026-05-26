class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        fleets = 0
        prev_time = 0

        for pos, speed in cars:
            time = (target - pos) / speed
            if time > prev_time:
                fleets += 1
                prev_time = time
        
        return fleets

        