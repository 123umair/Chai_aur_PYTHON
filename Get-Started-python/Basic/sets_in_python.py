# sets is a collection of unordered items.Each element in the set must be unique and immutable.
# In Python, a set is a mutable collection, meaning you can add or remove items after its creation.
# However, the elements inside a set must be immutable (e.g., numbers, strings, tuples).
# This means you cannot have lists or other sets as elements inside a set.
# Sets automatically remove duplicate values and do not maintain any order.
# You can use methods like .add() to insert new elements, and .remove() or .discard() to delete elements.
# Sets are useful when you need to store unique items and perform operations like union, intersection, and difference.
first_set = {1,2,3,4,5,6}
print(first_set)
print(type(first_set))

# set cannot take a duplicate elements  it will autmatically remove the duplicate items here... lets prove it..
duplicate_set = {1,2,3,4,5,6,7,5,3,5}
print(duplicate_set) # {1, 2, 3, 4, 5, 6, 7} so there the output of the set is that it will give only the output of the unique item....


# Create one new mix set

mix_set = {'umair',2,5,3,'Appifytech'}
print(mix_set)



# CREATE EMTPY SET 

blank_set = {}  # but this is wrong syntax of creating an emtpy set because this is the sytax of the dictionary if u check the type then it will dictionary type
print(type(blank_set)) # <class 'dict'>

# the correct syntax of the emtpy set is 
empty_set = set()
print(empty_set) # set()
print(type(empty_set)) # <class 'set'>



# set methods 
# set.add(el) #adds an element
# set.remove(el) #removes the elemant
# set.clear() #empties the set
# set.pop() #removes a random value
# set.union(give_one_set) #combines both set values and returns new
# set.intersection(give_one_set) #combines common values and return new

set_one ={1,2,4,5,5,6,7}
set_one.add("hello g")
print(set_one)


# remove method is removed the items from the set that u will give in parenthesis
set_one.remove(2)
print(set_one)  # now 2 will be removed from them

# clear method will clear your set
# set_one.clear() # empty set will be returned
# print(set_one)

# pop() method will be randomly removed the items from them 
print(set_one.pop())
print(set_one)


# one lets working on the set union method
set1 = {"fruit","Vegetables","Tea"}
set2 = {40,50,60}
union_set = set1.union(set2)
print(union_set)

# intersection method
set_no1 = {1,2,3,4}
set_no2 = {1,2,3,4,5}   # common are 1,2,3,4
intersection_set = set_no2.intersection(set_no1)
print(intersection_set)
