# now we learing inheritance now ok
class Parent:
    def  __init__(self,name,age,skill):
        self.name = name
        self.age = age
        self.skill = skill
    def method(self):
        return (f"{self.name } is the father of the shakir and its age is {self.age} year old and its skill is {self.skill}")



class Child(Parent):
    def  __init__(self, name, age, skill,language):
        super().__init__(name, age, skill) #this properties is include in the parent class and language will be the new property of the child class there for we not include it in the superclass because super class copy the properties from the parent class
        self.language = language
    def intro(self):   # here the self keyword is worked as a this keyword in js and give the current context
        return f"My name is {self.name} and my age is {self.age} and my skill is {self.skill} and the language i will use during communication with different people {self.language}"



object = Parent('Jhone Doe',55,"Web Developer") #this is the parent object
childObject  = Child('shakir',24,'Data Sciencetist','Native,English,Spanish')
print(object.method())
# print(childObject.name,childObject.age,childObject.language,childObject.skill)
print(childObject.intro())