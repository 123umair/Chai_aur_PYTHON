# Now we or working on the static method that means the method in a class only accessible for the class but not for the class instance this static method is also called the decorator  

# create one a simple class

class Car:
    total_car = 0
    def __init__(self,brand,model,fuel):
        self.brand = brand
        self.model = model
        self.fuel  = fuel
        Car.total_car = Car.total_car + 1   # here we are adding the total car to 1
    def Method(self):
        return f"This is the Car detail: {self.brand} {self.model} {self.fuel}"

    @staticmethod
    def class_Method():
        return f"Here this is the class static method that only accessed by class not by intance of the car class"
car_Object = Car('Honda_civic','2025','diesel and petrol')
# print(car_Object.Method())
print(car_Object.class_Method())
# print(Car.class_Method())