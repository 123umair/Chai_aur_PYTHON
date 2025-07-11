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