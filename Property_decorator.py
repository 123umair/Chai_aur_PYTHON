# so here property decorator is working like access the method as a property not by calling specially private vairable in the give example... check....

class Books:
    def __init__(self,title, author, pages):
        self.__title = title #title will be private and assign to the variable title
        self.author = author
        self.pages = pages
    def method(self):
        return f"{self.author}{self.pages}"
    @property
    def title(self):        #these method will be accessed as a property....
        return self.__title
obj_Book = Books('bange dara','allama iqbal',500)
print(obj_Book.title)
# print(obj_Book.method)
# print(obj_Book.title())