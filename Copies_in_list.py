# Shallow Copy and Deep copy concept in List 
a = [1,2,3,4,5]
b = a   # here b also point to the reference of a we can print it now
# print(id(a)) #1444976355008  address of a
# print(id(b)) #1444976355008 address of a 

# one another point inside the list the items also have its own memory address assigned to it like we access first element also check it address inside the list every item have also separate address 
# print(a[0], ': adddress of item a inside the list' , id(a[0])) # 1 : adddress of item a inside the list 140728658314152
# print(a[1], ': adddress of item a inside the list' , id(a[1])) # 2 : adddress of item a inside the list 140728658314184
# print(a[2], ': adddress of item a inside the list' , id(a[2])) # 3 : adddress of item a inside the list 140728658314216

# Let's see what happens when we change an element in 'b'.
# Since 'b' is just another reference to the same list as 'a', modifying 'b' will also affect 'a'.
b[0] = 9  # Change the first element of 'b' to 9
#
# As you can see, both 'a' and 'b' reflect the change.
# This is because they both point to the same list object in memory.
# So this is shallow copy


# now we use the .copy() method
original_list = ['umair','khan','laptop','Toshiba']
copylist = original_list.copy()
# print(original_list)
# print(copylist)
# print("id of originallist : ",id(original_list))   # 2012528683584
# print("id of copylist :" ,id(copylist)) # 2012530129920


# As shown above, when we use the .copy() method, it creates a new list with the same elements as the original,
# but the new list has a different memory address. This means changes to one list will not affect the other.
# The .copy() method is useful when you want to duplicate a list and work with the copy independently of the original.

# copylist[0] = 1 
# print(copylist)
# print(original_list)  #not effected because both list have different memory addreses this is deep copy



###################  but .copy() create again a shallow copy on the nested lists  ######################

nest_list = [[2,3],['umair','nestedlist']]   # now the outer list have its own copy and the inside the lists have another memory address

copy_nest_list = nest_list.copy()

# print(nest_list, 'address : ', id(nest_list)) #2342079009344 both have different memory address but the  inner items addresses are  same check it 
#print(copy_nest_list, 'address : ', id(copy_nest_list))  # 2342079009408

#print(id(copy_nest_list[0])) # same address 2221258082624
#print(id(nest_list[0]))  # same address of both 2221258082624

# now if we change the nested list in one copynestlist then its effect the nested list of the parent nested list due to same addresses  inside of the items in a both outer lists
copy_nest_list[0][0] = 'newitem' 
#print(copy_nest_list) # effected
#print(nest_list)    # This is affected because .copy() only makes a shallow copy. 
# If you want to avoid this effect (i.e., changes in nested lists affecting both copies), you should use the deepcopy() method.

# The deepcopy() method is available in the 'copy' module. It creates a completely independent copy of the original list, 
# including all nested objects. This means changes to nested elements in the copy will NOT affect the original.

import copy
unique_items = [["toshiba","lenovo"],["Macbook","Hp"]]
deepcopy_items = copy.deepcopy(unique_items)
deepcopy_items[0][0] = "Dell"
print(deepcopy_items)
print(unique_items) # not effectec
print(id(unique_items[0])) #different memory address
print(id(deepcopy_items[0])) #memoary address will different
