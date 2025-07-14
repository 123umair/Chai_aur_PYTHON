# # while loop
# # i = 1 #iterator
# # while i<=10:  #condition  #overall process is iteration
# #     print('hello g')
# #     i = i+1 #increment
    
#     # Q1 : Print numbers from 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i += 1

#     # Q2 : Print numbers from 100 to 1
# i = 100
# while i >=1:
#     print(i)
#     i -= 1

#     # Q3 : Print the multiplication table of a number n.
# n = int(input('Enter the number and print the table '))
# i = 1
# while i <=10:
#     print(i,"*",n,"=",n*i)
#     i =i + 1

      # Q4 : Print the elements of the following list using a loop.
     #   [1,4,9,16,25,36,49,64,81,100]
# list = [1,4,9,16,25,36,49,64,81,100]
# index = 0
# while index < len(list):
#     print(list[index])
#     index = index+1

    # Q5 :  Search for a number x in this tuple using loop.
    # tuple_list = (1,4,9,16,25,36,49,64,81,100)



# tuple_list = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i<len(tuple_list):
#     if (tuple_list[i] == x):
#         print('Founded the targeted value 36 at index',i)
#     i = i+1

# Break and Continue
# How it works:
# 'break' will stop the loop immediately.
# 'continue' will skip the current iteration and move to the next one.
# If the user wants to perform a specific task only when skipping an iteration, the 'continue' keyword can be used.

#example no.1 Break
# fruit_list = ["Mangoe","Apple","Banana","Lichiee"]
# i = 0
# while i<len(fruit_list):
#     if(fruit_list[i] == "Banana"):
#         print("This fruit present in the list")
#         break                      # but here at this point statement will be true and now break statement will execute and ignore the below the statements
#     else:
#         print("Not present")   # for first 2 iterations it will not present here this else statement is executed 
#     i = i+1
# print('Break statement is executed and now else part is terminate')

#example no.2 Continue statement
# Example: How the 'continue' statement works in a loop

# chai_list = ["Masala Chai", "Adrak Chai", "Butter Tea", "Sulaimani Chai", "Sulaimani Chai"]

# i = 0
# while i < len(chai_list):
#     # Check if the current chai is "Sulaimani Chai"
#     if chai_list[i] == "Sulaimani Chai":
#         print('Present your favourite chai at index', i)
#         # 'continue' will skip the rest of the code in this iteration and move to the next one
#         i = i + 1  # increment before continue to avoid infinite loop
#         continue
#     # This line will only run if the current chai is NOT "Sulaimani Chai"
#     print("Not present these chai type at index", i)
#     i = i + 1  # increment for the next iteration

# # Exmaple no.3 Now we check on the even and odd concept
# i = 0
# while i < 10:
#     if(i%2==0):
#         print(i, 'the even number')
#         i = i+1
#         continue
#     print(i, "This is odd numbers")
#     i=i+1



# For Loop are used for sequential traversal (one after another), For traversing list,string,tuples etc.
# For Example: 
# name_list = ['umair','skills','AppifyTech']
# for names in name_list:  # here all the items inside the list will assign to the varaible name and will print one by one here.
#     print(names)   

# check string

# string = "University of Science and Technology Bannu"
# # now u will travers every characters one by one here.
# for char in string:
#     print(char)
# # add one condition here 
# string_two = "AppifyTech innovation and exellence"

# count = 0  # count ko loop ke bahar initialize karo

# for char in string_two:
#     if char == "e":
#         count += 1  # count ko 1 se badhao jab bhi "e" mile

# print('"e" is found', count, 'times')


# Print the elements of the following list using a loop:

# #   [1,4,9,16,25,36,49,64,81,100]
# numbers = [1,4,9,16,25,36,49,64,81,100]
# for nums in numbers:
#     print(nums)

# #search for a numbers x in this tuple using loop
# tuple_numbers = (1,4,9,16,25,36,49,64,81,100)
# x=100
# i = 0
# for nums in tuple_numbers:
#     if( nums == x):
#         print('PRESENT THE TARGETED VALUE HERE AT INDEX',i)
#     i=i+1
   
    
# print('Finish loop')


# range():  Range functions return a sequence of numbers, starting from 0 by default, and increments by 1 (by default),and stops before a specified number.
# range(start?,stop,step?)
# seq=range(5)
# # print(seq[0])
# # print(seq[1])
# # print(seq[2])
# # print(seq[3])
# # print(seq[4])

# for i in seq:
#     print(i)

# print numbers from 1 to 100

# for i in range(1,101):
#     print(i)


# print numbers from 100 to 1;

# for i in range(100,0,-1): # decreased by -1, and stepsize will be negate or positive. 
#     print(i)

# print the one table of n
# n = int(input("Enter the table number:"))
# for i in range(0,11):
#     print(i,"*",n,"=",i*n)


# WAP that will the sum of the n natural numbers
# n = 7
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

# # now again write this program on a while loop
# n = 7
# i = 1
# sum = 0
# while i <= 7:
#     sum = sum + i
#     i = i+1
# print(sum)

#WAP THAT WILL FIND THE FACTORIAL OF A NUMBER n

n=3
fact = 1;
for i in range(1,n+1):
    fact = fact * i
print(fact)