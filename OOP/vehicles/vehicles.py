class Vehicle():
    def __init__(self, size, capacity, topspeed):
        self.__size = size
        self.__capacity = capacity
        self.__topspeed = topspeed
    
    def getSize(self):
        return self.__size
    
    def getCapacity(self):
        return self.__capacity
    
    def getTopspeed(self):
        return self.__topspeed
    
    def outputData(self):
        return (self.__size, self.__capacity, self.__topspeed)

class Car(Vehicle):
    def __init__(self, size, capacity, topspeed, wheels=4, doors=3):
        super().__init__(size, capacity, topspeed)
        self.__wheels = wheels
        self.__doors = doors
    
    def getWheels(self):
        return self.__wheels

    def getDoors(self):
        return self.__doors

    def outputData(self):
        return (self.__size, self.__capacity, self.__topspeed+"mph", self.__wheels, self.__doors)

class Ship(Vehicle):
    def __init__(self, size, capacity, topspeed, passengers, captain):
        super().__init__(size, capacity, topspeed)
        self.__passengers = passengers
        self.__captain = "Captain " + captain

    def getPassengers(self):
        return self.__passengers

    def getCaptain(self):
        return self.__captain

    def outputData(self):
        return (self.__size, self.__capacity, self.__topspeed, self.__passengers, self.__captain)