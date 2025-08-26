# Prectusing on the decorators......................

# def decorator(func):
#     def wrapper():
#         print('running the main function')
#         func()
#     return wrapper

# def mainFunct():
#     print("hi or hello im executed")

# execute = decorator(mainFunct)

# execute()

# here we will also use it like that
def decorator(func):
    def wrapper():
        print('running the main function')
        func()
    return wrapper


@decorator
def mainFunct():
    print("hi or hello im executed")

mainFunct()



# One another example... is that 



def decorator(func):
    def wrapper(user):
        print('proceeding......')
        if not user.get('is_loggedIn'):
            return 'access denied'
        return func(user)
    return wrapper


@decorator
def dashboard(user):
    return f'welcome  {user['name']}'


user1={'name':"m.umair",'is_loggedIn':True}
user2={'name':"m.hamza",'is_loggedIn':False}


print(dashboard(user1))








