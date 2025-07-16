# first_Dic = {'name':"umair","age":23}
# # print(first_Dic)
# # print(first_Dic["name"])
# # print(first_Dic.get('name'))
# #now check the by the if condition like
# if 'name' in first_Dic:
#     print(first_Dic["name"])

# #adding one another key value to the dictionary 
# first_Dic["newitem"] = "Chai"
# print(first_Dic) #{'name': 'umair', 'age': 23, 'newitem': 'Chai'}


# #now removing the items from the dictionary
# #pop() here in python you 
# first_Dic.pop("newitem") # Here it will remove the newitem with value
# # print(first_Dic)
# # first_Dic.popitem() # now this method will remove the last item from the dictionary
# # print(first_Dic)

# #now we will see the clear() method
# # first_Dic.clear()
# # print(first_Dic) #clear all the dictionary from the item

# WAP to enter the marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Uss subject name as key and marks as value.



emtpy_dictionary = {}
x = int(input("Enter Score : "))
emtpy_dictionary.update({"physics": x}) 
x = int(input("Enter Score : "))
emtpy_dictionary.update({"Maths": x}) 
x = int(input("Enter Score : "))
emtpy_dictionary.update({"Chemistry": x}) 
print(emtpy_dictionary)