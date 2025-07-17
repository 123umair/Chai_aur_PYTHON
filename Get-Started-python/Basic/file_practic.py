# Lets practice on file and solve the questions
# Create a new file "practice.txt" using python. Add the following data in it:
#     Hi everyone
#     we are learning File I/O
#     using Java.
#     I like programming in Java.
# WAF that replace all the occurrences of "java" with "python" in above file.abs

# Search if the word "learning" exists in the file or not.


f=open("practice.txt",'w')
write = f.write("Hi everyone \nwe are learning File I/O\nusing Java.\nI like programming in Java.")
f.close()



# now the task is that write a function that replace all the occurrences of "java" with "python" in above file.
# with keyword use
with open("practice.txt",'r') as f:
     data = f.read()
new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt",'w') as f:
    f.write(new_data)
f.close()

# Another task is that Search if the word "learning" exists in the file or not ?
# yahan data.find(word) != -1 ka matlab hai:
# agar "learning" word file ke andar maujood hai, to data.find(word) uski position (index) return karega (jo 0 ya us se bara hoga).
# agar word nahi milta, to data.find(word) -1 return karta hai.
# is liye, data.find(word) != -1 ka matlab hai: agar word mil gaya to True, warna False.

def word_checking():
    with open("practice.txt","r") as f:
         data = f.read()
         word = "learning"
    if(data.find(word) != -1): 
            print("Found")
    else:
            print('Not found')

word_checking()


# another task is WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found.
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
            while data:
                data = f.readline()
                if (word in data):
                        print(line_no)
                        return
                line_no +=1
    return -1
check_for_line()
# From a file containing numbers separated by comma,print the count of even numbers.


# create one another file that containing this numbers 1 , 2, 75, 84, 90, 101
# From a file containing numbers separated by comma,print the count of even numbers.
# here we open the numbers file

count = 0
with open("numbers.txt",'r') as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)
    
    
    
    
    
    
    
    
    
    
    # num = "" 
    # for i in range(len(data)):
    #     if(data[i] == ','):   
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i] 
