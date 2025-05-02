# Parent class 
class Vehicle: 
    def describe(self): 
        print("This is a vehicle.") 
 
# Child class inheriting from Vehicle 
class Car(Vehicle):   
    print("This is a car.") 
    pass  # Inherits everything from Vehicle 
 
# Creating an object of Car 
my_car = Car() 
 
# Calling the describe() method 
my_car.describe() 
