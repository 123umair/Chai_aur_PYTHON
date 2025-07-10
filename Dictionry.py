first_Dic = {'name':"umair","age":23}
# print(first_Dic)
# print(first_Dic["name"])
# print(first_Dic.get('name'))
#now check the by the if condition like
if 'name' in first_Dic:
    print(first_Dic["name"])

#adding one another key value to the dictionary 
first_Dic["newitem"] = "Chai"
print(first_Dic) #{'name': 'umair', 'age': 23, 'newitem': 'Chai'}


#now removing the items from the dictionary
#pop() here in python you 
first_Dic.pop("newitem") # Here it will remove the newitem with value
print(first_Dic)
first_Dic.popitem() # now this method will remove the last item from the dictionary
print(first_Dic)