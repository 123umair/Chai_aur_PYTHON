class Car:                                        #class constructor 
    def __init__(self,brand,model):
        self.model = model                                                  
        self.brand = brand
    def method(self):
        print(f"this is a {self.brand} {self.model} car")

class inherit(Car):
    def __init__(self, brand, model,batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize


newtesla = inherit('tesla','Model S','50kwh')
print(newtesla.brand,newtesla.model,newtesla.batterySize)
myCar = Car("China","toyota")
print(myCar.brand,myCar.model) #instance of Car
mynewCar = Car("Germany","BMW")  #instance of Car ....
print(mynewCar.brand,mynewCar.model)
print(mynewCar.method())   #add one another method and functionality to the class

#check txt notes for understanding 