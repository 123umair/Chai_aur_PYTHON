# # What is mixins?
# # Mixin ek class hoti hai jo apne aap me complete object nahi hoti, lekin dusri classes ko extra functionality dene ke liye banayi jaati hai. Matlab tumhe ek reusable code ka piece mil jata hai jo tum multiple classes ke andar reuse kar sakte ho.

# # Mixin is a class that will not completely object. but it will give extra funcitonality to another classes.Means by mixins we will find a reusable piece of code that will reuse in a multiple classes.

# class WalkMixin:
#     def walk(self):
#         print('walking..')

# class SwimMixin:
#     def swim(self):
#         print('Swimming......')


# class Duck(WalkMixin,SwimMixin):  # Inherit mixins
#     def sound(self):
#         print('Quack!')

# duck = Duck()
# duck.walk()
# duck.swim()
# duck.sound()


# Ek mixin jo seif functionality deta hy 

class LogMixin:
    def log(self,message):
        print(f"[LOG]:{message}")

class User:
    def __init__(self,username):
        self.username = username

    def show(self):
        print(f"User: {self.username}")



# Mixin + Normal Class to combine karna 

class LoggedUser(User,LogMixin):
    def save(self):
        self.log(f"Saving user {self.username}") # Mixin Method user kya 
        print("User saved!")
    
# Object Banana
u = LoggedUser('umairkhan')
u.save()
u.show()






class hardwork:
    def hardwork(self):
        print("Work hard...")

class std(hardwork):
    def __init__(self,name,address,role):
        self.name = name
        self.address = address
        self.role = role
    def __str__(self):
        return f"{self.name} address:{self.address} detail:{self.role}"
    
s1 =std('umair','bannu','appify Internee')
print(s1)
s1.hardwork()
        