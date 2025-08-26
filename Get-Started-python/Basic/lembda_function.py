# Anonymous function or lembda function 
#  A lambda function is also called the anonymous function.It is a small function that can be defined in a single line of code without a name.It is useful when we read a simple function that we don't want to define explicitly using the def keyword. The basic syntax of the lambda function in python is .

# lambda argument:expression
# Here arguments refers to the input arguments for the function and expression is a single expression that gets evaluated and returned as the result of the function. The result of the expression is automatically  returned by the lambda function, so there's is no need to use the returned statement.


# first we use a normal function and then we use the lembda function to  know which function is better for small works

# def add(x):
#     return x+4
# print(add(4))
# # ok now  i will do the same task on the lemda function

# add = lambda y:y+4
# print( 'lambda function is executed: ' ,add(4))

# now here find the length of the string 


len_string = lambda y:len(y)

print(len_string('umair'))


# Now convert a list of integers to their corresponding square values:
numbers=[1,2,3,4,5,6,7]
number_result = map(lambda x:x*2 ,numbers)
print(list(number_result))

# now convert a list of integers to their corresponding sqaure values
sqr_num=[1,2,3,4,5,6,7]
sqr_result = map(lambda x:x**2,sqr_num)
print(list(sqr_result))


# sorted a list of strings based on their alphabetical characters and length 
fruits = ['cherry','apple','banana','mangoe']

print(sorted(fruits,key=lambda x:len(x)))



people = [
    {'name':"umair",'age':"23",'occupation':'Internee'},
    {'name':"ABC",'age':"30",'occupation':'Manager'},
    {'name':"XYZ",'age':"28",'occupation':'Python developer'},
]

print(sorted(people,key=lambda x:(x['age'],x['name'])))


# find the maximum value in a dictionary

data = {'a':10,'b':20,'c':30}
max = max(data,key=lambda x:data[x])
print(max ,'our max value ')