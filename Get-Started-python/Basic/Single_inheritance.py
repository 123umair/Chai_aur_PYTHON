# Single Level Inheritance
class Mycar:
    @staticmethod
    def car_start():
        print('Car is starting.......')
    @staticmethod
    def car_stop():
        print('Car is stopped.......')
class Toyota_car(Mycar):
    def __init__(self,brand):
        self.brand = brand
        print(brand)
car1 = Toyota_car("Lamborghini")
car1.brand
car1.car_start()
car1.car_stop()



class Mobile:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print(self.name,self.price)  
    @staticmethod
    def about():
        print("Hello this is me umair khan this is the static method") 
    
name = Mobile('iphone promax','14lack')
name.about()


# Multilevel Inheritance Example
# In multilevel inheritance only one base class and inherit its properties to all the child classes.

class Animal:        # This is the Base class
    def eat(self):
        print("Animal is eating.")

class Mammal(Animal):
    def walk(self):
        print("Mammal is walking.")

class Dog(Mammal):
    def bark(self):
        print("Dog is barking.")

# Create an object of Dog class
dog = Dog()
dog.eat()   # Method from Animal
dog.walk()  # Method from Mammal
dog.bark()  # Method from Dog



# Explanation of the code flow:

# 1. A Parent class is defined with an __init__ method that initializes three attributes: name, age, and rol.
class Parent:
    def __init__(self, name, age, rol):
        self.name = name
        self.age = age
        self.rol = rol

# 2. A Child class is defined that inherits from Parent.
#    - Its __init__ method takes four parameters: name, age, rol, and relation.
#    - It calls the Parent's __init__ method using super() to initialize name, age, and rol.
#    - It then initializes its own attribute, relation.
class Child(Parent):
    def __init__(self, name, age, rol, relation):
        super().__init__(name, age, rol)
        self.relation = relation

    # 3. The about() method prints a message using the name and relation attributes.
    def about(self):
        print(f"This is the son of the {self.name} and its work as a software engineer in this company its relation is {self.relation}")

# 4. An object 'son' of the Child class is created with the following values:
#    - name: 'Imran'
#    - age: '22'
#    - rol: 'sofware enginner'
#    - relation: 'son'
son = Child('Imran', "22", 'sofware enginner', 'son')

# 5. The about() method of the 'son' object is called, which prints the formatted message.
son.about()

# 6. The 'son' object itself is printed. Since the Child class does not define a __str__ or __repr__ method,
#    this will print the default object representation, such as <__main__.Child object at 0x...>
print(son)





# Multiple inheritance
# Consist of more than one base_class. 
class A:
    varA = "This is varA"
class B:
    varB = "This is varB"
class C(A,B):
    varC = "Welcome This is varC"
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


# Again working on a super()
# Super method: super() method is used to access methods of the parent class.
class Fan:
    def __init__(self,type):
        self.type = type # i want this type is accessible in the child class khurshid


    @staticmethod
    def start():
        print("fan is start......")
    
    @staticmethod
    def stop():
        print("fan is stop......")
class khurshidfan(Fan):
    def __init__(self,brand,type):
        super().__init__(type)
        self.brand = brand
        super().start() #parent static method calling syntax
khurshid = khurshidfan("Khurshid","AC/DC")
khurshid.start()
print(khurshid.brand)
print(khurshid.type)

# class decorator 
# class method a class method is bound to the class and receives the class an an implicit first argument.
# Note - static method can't access or modify class state and generaly for utility

# class Detail:
#     student_name = "Muhammad_Umair_khan"
#     # now i want to change this vairalbe
#     def changeName(self,student_name):
#         # # self.student_name = student_name
#          self.__class__.student_name = student_name #change self.__class__ means self.Detail instead of this to change the class attributes we use easily the classmethod dercorator

# std = Detail()
# std.changeName("umair_appify_tech")
# print(std.student_name) # change now instead of this use easily the @classmethod we can take this example again as a simply



# class Detail:
#     student_name = "Muhammad_Umair_khan"
#     # now i want to change this classattribute
#     @classmethod
#     def changeName(cls,student_name):
#         cls.student_name = student_name
 
# std = Detail()
# std.changeName("Appifytech umair")
# print(std.student_name)  # changed easily



# propety decorator when we use a method in a class as a property 
# In the original code, the percentage was calculated once in the constructor and stored in self.perc.
# So, if you changed the marks later, self.perc would not update, and you'd get the same result.
# To fix this, we use a @property so that perc is always calculated from the current marks.

class Marks:
    def __init__(self, phy, eng, cs):
        self.phy = phy
        self.eng = eng
        self.cs = cs
        # self.prc = str((self.phy + self.eng + self.cs) / 3) + "%"
    @property
    def perc(self):
        return str((self.phy + self.eng + self.cs) / 3) + "%"
   # here u will access the method as a property and now i will use it simply with good syntax and it will give the update value 

stumark = Marks(89, 98, 34)
print(stumark.perc)
# now if I change the marks, the percentage will update accordingly
stumark.phy = 96
print(stumark.perc)  # now it gives the updated result

