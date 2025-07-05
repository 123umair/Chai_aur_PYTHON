# When we initialize any variable in python with double underscore __  then this vairable will be private like __hello = 'somethng' now this vairable is private
# And this vairalbe will be access during the class and not accessible for any instace or object of the class.
class Encapsulation:
    def __init__(self,name,age):
        self.__name = name
        self.age = age   #now this vairable is not  private now we will access its outside the class easily
    def Method(self):
        return f"{self.__name}"

object = Encapsulation('umair',38)
#  It will give the value 38
print(object.age)  
# Correct way 1: Using the class method
print("Accessing through method:", object.Method())
# Correct way 2: Using name mangling
print("Accessing through name mangling:", object._Encapsulation__name)


