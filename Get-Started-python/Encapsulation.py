# When we initialize any variable in python with double underscore __  then this vairable will be private like __hello = 'somethng' now this vairable is private
# And this vairalbe will be access during the class and not accessible for any instace or object of the class.
class Encapsulation:
    def __init__(self, name):
        self.__name = name
    def Method(self):
        return f"{self.__name}"

object = Encapsulation('umair')
# Correct way 1: Using the class method
print("Accessing through method:", object.Method())
# Correct way 2: Using name mangling
print("Accessing through name mangling:", object._Encapsulation__name)
