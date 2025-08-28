# # Dundar function..
# Part1 without use of the dundar function 
# class Complex:
#     def __init__(self,real,imagionary):
#         self.real = real
#         self.imagionary = imagionary                                                              
    
#     def showNumber(self):
#         print(self.real,'i +',self.imagionary,'j')
    
#     def add(self,num2):    # self num1 object araha hy or num2 tho hy dusra object 
#         newReal = self.real + num2.real
#         newImg = self.imagionary + num2.imagionary
#         return Complex(newReal,newImg)   # This object is return to the num3 where added values of real and imagionary part ......

# num1 = Complex(1,2)
# num1.showNumber()
# num2=Complex(2,4)
# num2.showNumber()
# num3 = num1.add(num2)
# num3.showNumber()



# Part2 Using of Dundar Function... also called the operator overloading .

# class Complex:
#     def __init__(self,real,imagionary):
#         self.real = real
#         self.imagionary = imagionary                                                              
    
#     def showNumber(self):
#         print(self.real,'i +',self.imagionary,'j')
    
#     def __add__(self,num2):    # self num1 object araha hy or num2 tho hy dusra object 
#         newReal = self.real + num2.real
#         newImg = self.imagionary + num2.imagionary
#         return Complex(newReal,newImg)   # This object is return to the num3 where added values of real and imagionary part ......
    
#     def __sub__(self,num2):
#         newReal = self.real - num2.real
#         newImg = self.imagionary - num2.imagionary
#         return Complex(newReal,newImg)



# num1 = Complex(1,2)

# num1.showNumber()

# num2=Complex(2,4)

# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()
# num3 = num1 - num2
# num3.showNumber()


# one another example of a student detaill ...ok

# class Student:
#     def __init__(self,name,age,role):
#         self.name = name
#         self.age = age
#         self.role = role
#     def show(self):
#         print(f"My name is {self.name} and my age is {self.age} and role is {self.role} ")
# std_object = Student("Umair",23,"Internee at Appify")
# std_object.show()


class Student:
    def __init__(self,name,age,role):

        self.name = name

        self.age = age

        self.role = role

    def __str__(self):

        return (f"My name is {self.name} and my age is {self.age} and role is {self.role} ")

std_object = Student("Umair",23,"Internee at Appify")

print(std_object)  # so this is the benefit of dundar function that we can't manually call the meethods like std_object.show() dundar function will give me a good readability





# now we add two another dundar function __eq__ and __le__ dundar to check the lenght of the studentname and compared students


# class Student:
#     def __init__(self,name,age,role):

#         self.name = name

#         self.age = age

#         self.role = role

#     def __str__(self):

#         return (f"My name is {self.name} and my age is {self.age} and role is {self.role} ")
    
#     def __eq__(self, other):
#         return self.age == other.age and self.role == other.role
    
#     def __len__(self):
#         return len(self.name)
            

# std1 = Student("Umair",23,"Internee at Appify")
# std2 = Student("Hamza",23,"Internee at Appify")
# print(std1 == std2)
# print(len(std1))


# One another example part1 .. without use of a dundar function 
class Addition:
    def __init__(self,num1,num2):
            self.num1 = num1
            self.num2 = num2
    def add(self):
         newNum = self.num1 + self.num2
         return newNum
add_num = Addition(4,5)
print(add_num.add())


# Part 2 of these example
# __add__ ka kaam do objects ke beech + operator ko define karna hai.
class Addition:
    def __init__(self,num1,num2):
            self.num1 = num1
            self.num2 = num2
    def __add__(self,other):
         return (self.num1 + self.num2) + (other.num1 + other.num2)
add_num = Addition(4,5)
add_num2 = Addition(4,5)
result = add_num + add_num2
print(result)