class RaceCar():
    def __init__(self, colour, fuel_remaining):
        self.colour = colour
        self.fuel_remaining = fuel_remaining
        self.laps = 0
    
    def run_lap(self, length):
        self.fuel_remaining -= length*0.125
        self.laps += 1

if __name__ == "__main__":
    car = RaceCar("Silver", 23)
    print(f"{car.colour = }")
    print(f"{car.fuel_remaining = }")
    print(f"{car.laps = }")
    car.run_lap(13)
    print(f"{car.fuel_remaining = }")
    print(f"{car.laps = }")