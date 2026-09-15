from rental import Vehicle, Renter, ElectricCar, Motorbike

car = Vehicle("Toyota", "Yaris", "1AB234")
ecar = ElectricCar("Tesla", "Model 3", "2EV555", 75)
bike = Motorbike("Honda", "Wave", "3MB999", 125)
renter = Renter("Somchai P.", 998877)

print(car)
print(ecar)
print(bike)

car.rent()
print(car)     
car.return_vehicle()
print(car)       

try:
    Renter("", 123)
except ValueError as e:
    print("Caught:", e)

try:
    Renter("Jane", -5)
except ValueError as e:
    print("Caught:", e)

fleet = [car, ecar, bike]
for v in fleet:
    print(v)