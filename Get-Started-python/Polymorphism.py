# now We are working on the polymorphism


class Car:
    def __init__(self,brand,model,fuel):
        self.brand = brand
        self.model = model
        self.fuel  = fuel
    def fuel_type(self):
        return self.fuel
class Tesla(Car):
        def __init__(self, brand, model, fuel):
             super().__init__(brand, model, fuel)
        def fuel_type(self):
            return self.fuel
        
Car_obj = Car('toyota','old','petrol and diesel')
Tesla_obj = Tesla('Tesla','Advanced model','Electric Charge')
print(Car_obj.fuel_type())
print(Tesla_obj.fuel_type())