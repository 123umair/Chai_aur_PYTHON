# now We are working on the polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class Car:
    total_car = 0
    def __init__(self,brand,model,fuel):
        self.brand = brand
        self.model = model
        self.fuel  = fuel
        Car.total_car = Car.total_car + 1   # here we are adding the total car to 1
    def fuel_type(self):                               # method fuel_type
        return self.fuel
class Tesla(Car):
        def __init__(self, brand, model, fuel):
             super().__init__(brand, model, fuel)
        def fuel_type(self):                         # method fuel_type also used here this is polymorphism
            return self.fuel
        
Tesla_obj = Tesla('Tesla','Advanced model','Electric Charge')
Car_obj = Car('toyota','old','petrol and diesel')
New_obj = Car('toyota','old','petrol and diesel')
New_obj = Car('toyota','old','petrol and diesel')

print(Car_obj.fuel_type())
print(Tesla_obj.fuel_type())
print(Car.total_car)