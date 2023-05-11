class Building:
    pass

class House(Building):
    def __init__(self, pFloors, pWidth, pHeight, pBedrooms, pBathrooms):
        super.__init__(pFloors, pWidth, pHeight)
        self.bedrooms = pBedrooms
        self.bathrooms = pBathrooms

