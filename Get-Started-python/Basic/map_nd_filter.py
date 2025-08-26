# Map function: so map function in python is used to apply a specific function to each element of an iterable (like a list,tuple,or set) and returns a map object (which is an iterator)

# syntax of the map function :
# map(function,iterable)
# So now first we clarify  that what is iterable and what is iterator
# Iterable: is an object that we will use in a loops like for loop in python ....
# Iterator: is an object that return every single element of the iterable object ...

# Basic Example
# Let's start with a simple example of using map() to convert a list of strings into a list of integers.
s = ['1','2','3','4','5']
check=map(int,s)
print(check) # <map object at 0x000001D2B32DB940>   by the definition that it will return a map object 
print(list(check)) # u will convert into the list 

# Converting map object to a list
# By default, map() function returns a map object, which is an iterator. In many cases, we will need to convert this iterator to a list to work with the results directly.


# one another example 
# we will use a custome function and from the function we will multiply the 2 to the lists using the map function 
# now the give list is l=[1,2,3,4,5,6,7,8]


l=[1,2,3,4,5,6,7,8]

def multiple(val):
    return  val*2

result = list(map(multiple,l)) # Here multiple applies on every element of the iterable object l 
print(result)


# Now we use a lambda function instead of the custom function to make code shorted and easier.

b = [1,2,3,4,5]
new = list(map(lambda x:x*2,b))  # now here in this example b is the iterable object and the x is the iterator that will iterate each element of the b iterable object and multiply with 2 where lambda will wrapped into the map method so first lambda will be a iterator object for the b iterable object 
print(new)


# map() with multiple iterables

# We can use map() with multiple iterables if the function we are applying takes more than one argument.

c=[1,2,3,4]
d=[5,6,7,8]

final_result = map(lambda x,y:x+y,c,d)
print(list(final_result),'final result') # Explanation: map() takes x from a and y from b and adds them.

# Converting strings to Uppercase
fruits = ['Apple','Orange','Grapes']
res = map(str.upper,fruits)
print(list(res))

# Extracting first character from strings
words = ['Apple','Orange','Grapes']
newres = map(lambda s:s[0],words)
print(list(newres))

# Explanation: lambda s: s[0] extracts first character from each string in the list words. map() applies this lambda function to every element, resulting in a list of the first characters of each word.


# Removing whitespaces from strings
s = [' hello ',' world ',' python ']
new_res = map(str.strip,s)
print(list(new_res))
# Explanation: str.strip method removes leading and trailing whitespaces from each string in list strings. map() function applies str.strip to each element and returning a list of trimmed strings.




## Now we are working on the filter function if u can't understand are you want a simple example on the filter function then u will be first see the makrdown file filter.mkd 

# Example 1: Using filter() with a Named Function
# This code defines a regular function to check if a number is even and then uses filter() to extract all even numbers from a list.

# def even(n):
#     return n % 2 == 0
# nums_for_even = [1,2,3,4,5,6,7]

# even_result = filter(even,nums_for_even)
# print(list(even_result))


# Example 2: Using filter() with a Lambda Function
# no = [1,2,3,4,5,6,7]
# new_even_result = filter(lambda x:x % 2 == 0, no)
# print(list(new_even_result),'no')


# Example 3: Filtering and Transforming Data
no = [1,2,3,4,5,6,7]
new_even_result = filter(lambda x:x % 2 == 0, no)
transform = map(lambda X:X*2,new_even_result)
print(list(transform))
# Explanation:
# filter(lambda x: x % 2 == 0, a): Selects only even numbers from the list ([2, 4, 6]).
# map(lambda x: x * 2, b): Doubles each of the filtered even numbers ([4, 8, 12]).


# Example 4: Filtering Strings
a = ["apple", "banana", "cherry", "kiwi", "grape"]
len_word = map( lambda x:len(x) > 5,a)
lenth_word = filter( lambda x:len(x) > 5,a)
print(list(len_word),'map')
print(list(lenth_word),'filter')



# Example 5: Filtering with None (Truthiness Check)
# This code uses filter() with None as the function to remove all falsy values (like empty strings, None and 0) from a list.
L = ["apple", "", None, "banana", 0, "cherry"]
A = filter(None, L)
print(list(A))

# Output
# ['apple', 'banana', 'cherry']
# Explanation: filter(None, L) keeps only truthy values (non-empty strings, non-zero numbers, non-None values).



