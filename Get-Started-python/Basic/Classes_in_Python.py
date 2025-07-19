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

class Acount:
    def __init__(self,balance,acount_no): #constructor
        self.balance = balance
        self.acount_no = acount_no
    def debit(self,amount):       
        self.balance = self.balance - amount
        print("Rs.",amount,"was credited")
    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs.", amount,"was credited")
    def get_balance(self):
        return self.balance
acc1 = Acount(100000,1234567859)
acc1.debit(500)
print(acc1.get_balance())


