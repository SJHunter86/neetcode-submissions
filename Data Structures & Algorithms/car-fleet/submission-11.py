class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        fleet_time = 0

        for pos,spd in cars:
            arrival = (target-pos) / spd
            if arrival > fleet_time:
                fleets += 1
                fleet_time = arrival
        
        return fleets
