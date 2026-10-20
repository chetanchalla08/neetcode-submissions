class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse = True)
        
        fleet_time = 0
        fleets = 0

        for pos, spd in cars:
            time = (target - pos)/spd

            if time > fleet_time:
                fleets += 1
                fleet_time = time
            
        return fleets
                
