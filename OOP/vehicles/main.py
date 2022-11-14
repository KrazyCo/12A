from vehicles import *

print("f i e s t a")

fiesta = Car(3, 5, 110, 4, 5)
print(f"{fiesta.getSize() = }")
print(f"{fiesta.getCapacity() = }")
print(f"{fiesta.getTopspeed() = }")
print(f"{fiesta.getWheels() = }")
print(f"{fiesta.getDoors() = }")

print("\n\nb o a t")

boat = Ship(420000, 2521, 328475698405745869, "like none lmao we losing money", "Deez Nuts (dr)")
print(f"{boat.getSize() = }")
print(f"{boat.getCapacity() = }")
print(f"{boat.getTopspeed() = }")
print(f"{boat.getPassengers() = }")
print(f"{boat.getCaptain() = }")