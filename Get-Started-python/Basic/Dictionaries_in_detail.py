# # DICTIONARY WITH DIFFERENT METHODS AND TYPECASTING
# my_dict = {
#     "name":"umair",
#     "subjects":{
#         "English" : 68,
#         "Islamiat" : 88,
#         "urdu" : 45
#     }
# }
# # print(my_dict["subjects"]["English"])
# # here get all keys of the dictionary
# print(my_dict.keys())
# # here get all the values of these dictionaries
# print(my_dict.values())
# # use Items() method it will return all tha (keys,values) pairs with keys in tuples
# print(my_dict.items()) #inside the dictionary it will give in pairs in tuple with key and its value
# #now you we can change its datatype called the typecasting like that:
# dict_in_list = list(my_dict.items())
# print(dict_in_list[0]) # here now we will access it in an order form and also give the output of key value pair in tuple by .item() methods
# Methods my_dict.Keys() #returns all keys of the dictionary
# my_dict.values() #returns all values of the dictionary
# my_dict.items() #returns all (key,val) pairs as tuples
# my_dict.get("key") #returns they kay accroding to value
# my_dict.update(newDict) #inserts the spedivied items to the dictionaries

# now apply one by one




# Why we use method get() to access the keys for the dictionary we can access it on a simple as a key with dictionary name like  that:
best_dict = {
    "name" : "Aljazeera",
    "books" :"python",
    "address" : "Bannu ghala mandi"
}

# i access the first item in a dictionary by normal method

# print(best_dict["name"]) # value  will be "Aljazeera"
print(best_dict.get("name")) # now by get() method it will give the same result
 # now then why we need the get method here because both give the result same 
 # but sometime when we type the wrong name of dictrionary or enter the wrong name of key then it will create a problem ...... 
 # and give error and can not run code after that like that
# # print(best_dict["name2"]) # here it will give the error and after no code will be executed.. When we working on a real life problem and have millions of codes then it will be create a problem and then will find these error will be dificult instead of these when we use the .get() method it will give the
# print(best_dict.get("name23"))  # None and also executed the codes after that .... prevent control from stoping here.... there fore we used the .getmethod()
# print("hello g")


# Here one another tricky dictionary because we know that dictionary will store multiple data types
d = { "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }
print(d["name"]) # Prajjwal
print(d[1])    # Python
print(d[(1,2)]) # [1,2,4]
# now we also use the get() method for that
print(d.get("name") , d.get(1), d.get((1,2))) 


#nested dictionary 
person = {
    "name": "John",
    "age": 30,
    "address": {
        "city": "New York",
        "country": "USA",
        "details": {
            "street": "123 Main St",
            "zip": "10001"
        }
    }
}
# Access this 
print(person["name"],person["address"]["details"]) # give the same output 
print(person.get("name"), person.get("address").get("details")) # both will give the same output
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


# here  we know that dictionary are mutable and unordered means it have no index but not include the cuplicate values so we can add some keys values and also we can mutate some values

update_dict = {
    "name" : "Muhammad_Umair_khan",
    "age" : 22,
    "role" : "internee in appify tech"

}
# We can change the name of umair
update_dict["name"] ="Sajid"
print(update_dict)  # now name wil overrided 
# add one another items here 
update_dict["ide"] = "cursor"
print(update_dict)



# create one dictionary and change its type to list and access the first elements
typeCast_Dict = {
    "name" :"umair",
    "future":"Coder",
    "Skills":"Excited to gain more skills" 
}

listdic = list(typeCast_Dict.items())
print(type(listdic)) # type will be list
print(listdic[0])

# Now we are working on the update method in dictionary

my_dict = {
    1 : "Software House",
    2 : "Internship role",
    3 : "Paid",
    4 : "City_Tower"
}

# let insert some keys values and try to inser one new dictionary
# my_dict[5] = "Web Developer"
# print(my_dict)
# now if i write these like that the new key assign to the new variable and now give this as a argument or param to the update method 
newitems = {  5 : "Web Developer"}
my_dict.update(newitems)
# now i will add one another dictionary
new_nestDict = {
    6 : {
        'name' :"umair",
        'graduation' :"2025 SEPTEMBER",
        'Institute_name' : "University of Science and Technology Banni Town Ship"
    }
}
my_dict.update(new_nestDict)
print(my_dict)




# Exercise on these and access different values 
# complex_dict = {
#     "company": "TechNova",
#     "founded": 2010,
#     "is_public": True,
#     "employees": {
#         "total": 250,
#         "departments": {
#             "Engineering": {
#                 "teams": [
#                     {
#                         "name": "Backend",
#                         "lead": "Alice",
#                         "members": ["Bob", "Charlie", "David"],
#                         "projects": [
#                             {
#                                 "name": "API Revamp",
#                                 "budget": 120000,
#                                 "status": "Ongoing",
#                                 "milestones": {
#                                     "design": "Completed",
#                                     "development": "In Progress",
#                                     "testing": "Pending"
#                                 }
#                             },
#                             {
#                                 "name": "Auth Service",
#                                 "budget": 50000,
#                                 "status": "Completed",
#                                 "milestones": {
#                                     "design": "Completed",
#                                     "development": "Completed",
#                                     "testing": "Completed"
#                                 }
#                             }
#                         ]
#                     },
#                     {
#                         "name": "Frontend",
#                         "lead": "Eve",
#                         "members": ["Frank", "Grace"],
#                         "projects": []
#                     }
#                 ]
#             },
#             "HR": {
#                 "head": "Mallory",
#                 "policies": {
#                     "leave_policy": {
#                         "annual_leave": 20,
#                         "sick_leave": 10,
#                         "work_from_home": True
#                     },
#                     "recruitment": {
#                         "open_positions": ["Data Scientist", "DevOps Engineer"],
#                         "interview_process": ["Screening", "Technical Round", "HR Round"]
#                     }
#                 }
#             }
#         }
#     },
#     "offices": [
#         {
#             "city": "New York",
#             "address": "123 Madison Ave",
#             "employees_count": 100
#         },
#         {
#             "city": "Berlin",
#             "address": "Alexanderplatz 4",
#             "employees_count": 50
#         }
#     ],
#     "stock_prices": {
#         "2022": [120.5, 123.0, 125.8],
#         "2023": [130.2, 128.0, 135.5]
#     },
#     "partners": None
# }
