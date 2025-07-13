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



# ################### Now we are Working on the Nested Dictionary ################## #
# in a nested dictionary the nested dictionary is created by assing a key and the place of value u will put the dictionary like that

item = {
    "name":"umair",
    "age":23,
    "address":{
        "city":"Bannu",
        "country":"pakistan",
        "another_dict":{
            "name" : "XYZ",
            "AGE" : 32
        }
    }
}
#first access the item dictionary 
print(item)
print(item["address"]["city"])

#NOW ACCESS THE THIRD ONE NESTED DICTIONARY INSIDE THESE DICTIONARY best way is that ..
print("Age" , ":",item["address"]["another_dict"]["AGE"])
#here when you access different nested keys inside the dictionaries then u will used get method in that way
print('name',":",item.get("address").get("another_dict").get("name"))

#now we will see the update() method
# item["age"] = 24
# print(item)