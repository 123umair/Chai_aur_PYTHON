# WAF that give the average of any number
# def Avg(a,b,c):
#     sum = a + b + c
#     avg = sum /3
#     print(avg)
# Avg(1,2,3)

# WAF to print the length of a list. (list is the parameter)
from traceback import print_tb


list = [1,2,3,4,5]
def len_List(list):
    print(len(list))


len_List(list)



# WAF to print the elements of a list in a single line. (list is the paramter)
# new_list = [1,2,3,4,5,6,7,8]
# def single_line(list):
#     for i in list:
#         print(i, end=" ")
# single_line(new_list)

# WAF to find the factiorial of n (n is the parameter)
# n = int(input("Enter the value of n:"))
# def factiorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     print('Factorial of n:',fact)
# factiorial(n)


# WAF  to convert  USD to INR
# n=float(input('Enter the Dollar $:'))
# def Converter(USD):
#     exchange_rate = 86.02
#     INR = USD * exchange_rate
#     print("Your entered amount in INR:" , INR)
# Converter(n)

# Lets now working on the Recurssion 
# Recurssion is the function that call itself
#This is recursive function
def show(n):
    if(n == 0): #This is basecase if this is not then the function will b paused in a infinite loop 
        return
    print(n)
    show(n-1)
show(5)