# # Class is a blueprint for creating  objects.... 
# class Student:
#     def __init__(self,name, age):  # This is constructor that always executed when create an object of this class if we write it or not it will be created and executed by python itself   
#         self.name = name
#         self.age = age

#     def my_name(self):
#         print(f"My name is {self.name}")
#     def my_age(self):
#         print(f"My age is {self.age}")
# obj_student = Student("umairkhan", 22)
# myname=obj_student.my_name()
# myage=obj_student.my_age()

# Q1: Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# class Student:
#     def __init__(self,name,physics,chemistry,maths):
#         self.name = name
#         self.physics = physics
#         self.chemistry = chemistry
#         self.maths = maths
#     def calculate_avg(self):
#         total_marks  = self.physics + self.chemistry + self.maths
#         avg = total_marks/3
#         print(f"self.name will take the average marks in this three subjects {avg}")
# std_obj = Student("umair",99,98,97)
# std_obj.calculate_avg()


# we can createed it by using loops and pass marks in a list





class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def calculate_avg(self):
        sum = 0
        for val in self.marks:
            sum = sum + val
        print("hi",self.name, "your avg score is:", sum/3)

std_obj = Student("umair",[97,98,99])
std_obj.calculate_avg()



# Create Account class with 2 attributes - balance and acount no.
# Create methods for debit,credit and printing the balance.

# class Acount:
#     def __init__(self,balance,acount_no): #constructor
#         self.balance = balance
#         self.acount_no = acount_no
#     def debit(self,amount):       
#         self.balance = self.balance - amount
#         print("Rs.",amount,"was credited")
#     def credit(self,amount):
#         self.balance = self.balance + amount
#         print("Rs.", amount,"was credited")
#     def get_balance(self):
#         return self.balance
# acc1 = Acount(100000,1234567859)
# acc1.debit(500)
# print(acc1.get_balance())



# PRIVATE attributes and methods:
# Conceptual Implementation in Python
# priavte attributes and methods are meant to be used ontly within the class and arenot accessible from outside the class.
# one example on private attributes is that
# class Account:
#     def __init__(self,acount_no,password):
#         self.acount_no = acount_no
#         self.password = password
#     def access_acountInfo(self):
#         print(f'YOUR PASSWORD IS {self.password} and your account_no is {self.acount_no}')
        

# acc_obj = Account("1235443","abcde1")
# acc_obj.access_acountInfo() 
# YOUR PASSWORD IS abcde1 and your account_no is 1235443

# this is not a goodprectus because this is so risky that every one see ur account password and name make them private
# so how i make it private
# there fore we create this program again that this will access only inside the class and direclty from the public
# Now you make the password private that will no one can access it.

# class Account:
#     def __init__(self,acount_no,password):
#         self.acount_no = acount_no
#         self.__password = password  # Account password is private...... 
#     def access_acountInfo(self):
#         print(f'YOUR PASSWORD IS {self.__password} and your account_no is {self.acount_no}')
#     # def get_password(self):  # method to access private variable
#     #     return self.__password

# acc_obj = Account("1235443","abcde1") 
# acc_obj.access_acountInfo() 

# Accessing the private variable using a method
# print("Accessing private password via method:", acc_obj.get_password())

# Accessing the private variable directly (not recommended, but possible with name mangling)
# print("Accessing private password via name mangling:", acc_obj._Account__password)



# we can create a private methods()

#like that

class newCar:
    def __init__(self, name, model, price, warranty):
        self.name = name
        self.model = model
        self.__price = price # instance variables


    def __priceMethod(self):
        print(self.__price)      # part of the object

    def access(self):
        self.__priceMethod()

    @staticmethod
    def static(warranty):
        print(warranty)

newCar_obj = newCar("Lamborghini", "2024", "90000$", "2year")
newCar_obj.access()
# Example usage of static method:
newCar.static("2year")


# create one a private method and also create one private vairable iside the whos the part of the object and access it 

class Role:
    def __init__(self,name,age,role):
        self.name = name
        self.age = age
        self.__role = role
    def __show_role(self):
        print(f"{self.name} and its role in {self.__role}")
    def access(self):
        self.__show_role()
role_obj = Role('umair','22','internee')
role_obj.access()


# Create one another private Static and access as a static method
# this is how a static method will be used 
class Static_method:
        @staticmethod
        def __hello():
            print("Hello g this is me ")
        @staticmethod
        def allowed():
            Static_method.__hello()
Static_method.allowed()