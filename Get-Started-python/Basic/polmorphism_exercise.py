# Q1: Define a Circle class to create a circle with radius r using the constructor.
# Defing an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

# import math
# class Circle:
#     def __init__(self,r):
        
#         self.r = r
#     def Area(self):
#         area_of_circle = math.pi * (self.r ** 2)
#         print(f"The area of the circle is {area_of_circle}  ")
#     def Perimeter(self):
#         perimeter_circle = 2*(math.pi)*(self.r)
#         print(f"The perimeter of the circle is {perimeter_circle}  ")
        
# obj_circle = Circle(21)
# obj_circle.Area()
# obj_circle.Perimeter()


class Circle:
    def __init__(self,radius):
         self.radius = radius
    def Area(self):
        return (22/7) * self.radius ** 2
    def Perimeter(self):
        return 2 * (22/7) * self.radius
obj_cir = Circle(21)
print(obj_cir.Area())
print(obj_cir.Perimeter())



# Q2: Define a Employee class with attributes roles, department and salary. This class also a showDetails() method.
#    Create an Engineer class that inherits properties from Employee and has additional attributes: name and age

class Employee:
    def __init__(self,role,department,salary):
        self.salary = salary
        self.role = role
        self.department = department
    def showDetails(self):
        print("Role = ",self.role)
        print("Department = ",self.department)
        print("Salary = ",self.salary)

class Engineer(Employee):
    def __init__(self, name , age):
        super().__init__("Engineer", "IT", "60000")
        self.age = age
        self.name = name
    


eng1 = Engineer(23,"Umair")
eng1.showDetails()




#Q3. Create a class called Orde which  stores item and its price.
# Use Dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2
# __gt__() is a dunder (double underscore) function used to compare two objects of a class.
# It allows you to define the behavior of the '>' (greater than) operator for your class.
# For example, order1 > order2 will return True if order1's price is greater than order2's price.

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,order2):
        return self.price > order2.price
order1 = Order("chips",300)
order2 = Order("lays",200)
print(order1 > order2) #true