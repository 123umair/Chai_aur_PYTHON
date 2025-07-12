thislist = ["apple", "banana", "cherry"]
print(thislist)

#accessed by indexing like that
print(thislist[-1])  # start slicing from the last items 
print(thislist[0]) # start indexing from the start items


# One another point is that list is mutable but tuple is not mutable ok...
# here now mutate the list u created
mutable_LIST =  thislist[0] = 'newfruit'
print(mutable_LIST)
print(thislist)   # ['newfruit', 'banana', 'cherry']

# here one another point to be remembere
print(thislist[1:2]) # ['banana']  # in slicing mode it will give the output  in array then u will change it and pass another item in an array not in ''STRING FORMATE 

thislist[1:2] = ["UMAIR"]  # NOW AT THE PLACE OF INDEX 1 IT WILL BE CHANGED AND NOW THE NAME OF THE ITEM IS UMAIR
print(thislist)

# if u will give in a string formate it will understand that every item in a string is array like that
thislist[1:2] = "UMAIR"
print(thislist) #['newfruit', 'U', 'M', 'A', 'I', 'R', 'cherry']


# here one another logical concept in the list 
# initialize new list
mylist = ["umair","intern","happy"]
print(mylist)

print(mylist[1:1])   # Output: []

# Now, if you assign a list to this empty slice, Python will insert the new items at that position (index 1).
# So, the two new items will be inserted at index 1, pushing the existing elements to the right.
mylist[1:1] = ["working on chatbot", "appifytech idea"]
print(mylist)
# Output: ['umair', 'working on chatbot', 'appifytech idea', 'intern', 'happy']

# In summary:
# - mylist[1:1] gives an empty list because there are no elements between index 1 and 1.
# - Assigning to mylist[1:1] inserts the new items at index 1, without removing any existing items.




#list methods
updated_list = ['bannu','lahore','barkat market','mainmarket'] #now we will use different methods that will remove,add,and delete items in python list
updated_list.append("CITY-TOWER")  
print(updated_list)   # append method will added the item in last of the os the list and will be made the last index of the list
#here u can applied the if state on that and check if u have city tower item in the list the print the the message i have city tower
if "CITY-TOWER" in updated_list:
    print("yes its present in our list in the last item")   # this will printed


# pop() in list how it will used to remove the items

updated_list = ['bannu','lahore','barkat market','mainmarket'] #u will remove the last item from them by pop
print(updated_list.pop()) #  these will printout the removed items
#remembered that the pop() will take an item in the dictionary but in the list it will not takes any item
print(updated_list) # this will give the updated list and now  at the indexing number will be reduced

# now we one workingon the insert method and cipy method and remove method
list2 = [1,2,3,4,5,6,5,True]
print(list2)

# The insert() method in Python lists is used to add an item at a specific position (index) in the list.
# Syntax: list.insert(index, item)
# - 'index' is the position where you want to insert the new item.
# - 'item' is the value you want to add.
# The existing elements from that index onwards are shifted to the right.
# Example:
# list2 = [1, 2, 3]
# list2.insert(1, 'a')  # Now list2 becomes [1, 'a', 2, 3]
list2.insert(1,'string')
print(list2)  #at index one it will add the 'string' item  


## now we used the remove method here how it work.... ok
# The remove() method in Python lists is used to delete the first occurrence of a specified value from the list.
# Syntax: list.remove(item)
# - 'item' is the value you want to remove.
# - If the item is not found, Python will raise a ValueError.
# Example:
list3 = [10, 20, 30, 20, 40]
list3.remove(20)  # Removes the first occurrence of 20
print(list3)      # Output: [10, 30, 20, 40]


## here one another example
list4 = ['umair','naveed','appifytech','umair','naveed']
print(list4)
# Now we use the removed that 
list4.remove('umair')
list4.remove('naveed')
print(list4)  # remvoe method will remove the  first occurences in the list 


# Working on the .copy() method

# The copy() method in Python is used to make a copy of a list.
# This means you get a new list with the same items, but it's a separate object in memory.
# So, if you change the original list, the copied list will NOT change.

# Example to show how it works:
Original_list = ["python", "Javascript", "reactjs"]

# Make a copy of the list using .copy()
copy_list = Original_list.copy()

# Now, Original_list and copy_list have the same items, but they are different lists.
# Let's add a new item to the original list:
Original_list.insert(3, "Flask")  # Adds "Flask" at the end of Original_list

# Print both lists to see the difference
print("Original_list after inserting 'Flask':", Original_list)
print("copy_list remains unchanged:", copy_list)

# Output:
# Original_list after inserting 'Flask': ['python', 'Javascript', 'reactjs', 'Flask']
# copy_list remains unchanged: ['python', 'Javascript', 'reactjs']

# So, .copy() is useful when you want to work with a copy of your list without affecting the original.