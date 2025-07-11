# Tuples are used to store multiple items and different data types in a single variable.
# A tuple is a collection which is ordered and unchangeable

#tuple cannot be mutable once you write values in tuple it can't be mutable or changed.
first_t = ("python","laravel","Reactjs")
print(first_t)

#Here you will be accessed by indexing different values like

print(first_t[0])
print(first_t[1])
print(first_t[2])


# you can add items to the tuple like
# Key point: A one-item tuple must have a comma: ("Fruit",) not ("Fruit").
one_item = ("oneItem",)

new_item = ("Fruit","Chai")  ## like that
more_item = first_t + new_item + one_item 
print(more_item)
(python,laravel,Reactjs,Fruit,Chai,oneItem)= more_item   #tuple distructuring ,tuple unpacking, Multiple assignment 



# one another tuple assignment or unpacking or destructuring is that 

item = ("umair","munib","naveed")
#again u can access through by the indexing
print(item[0]) #umair  
print(len(item))#one another logic that it i will used is that
if len(item) > 0:
    print(item[2]) # it will print  the naveed

#now destructurt it
(u,m,n) = item
print(u)
print(u,m,n) 