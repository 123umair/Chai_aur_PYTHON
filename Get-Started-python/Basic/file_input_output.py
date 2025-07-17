# f = open("demo.txt","r")
# data = f.read()
# print(data)
# f.close()


# Here some mode of file input and output

# 'r' open for reading (default).
# 'r+' this mode work as if u override a text from the start in the existing file then it work as a overiden text.
# 'w' open for writing, truncating the file first. 
# yaha ager hum kisi file may jab 'w' mode use krty hy. Tho jo meny file may lika hy usko overwrite kar k mery naye text, message waha pay write keeye jaty hy ... means wo delete ho jata hy or 'w' sy or neya uski jaga lika jata hy .....
# 'w+'   
# 'x' create a new file and open it for writing.

# 'a' open for writing,appending to the end of the file if it exists.
# ye 'a' mode is used for appending the txt to the end of the file and doesn't remove the old messages or text

# 'b' binary mode.
# This 'b' mode is used for open the binary file ...

# 't' text mode (default).
# if we open any text file then we used the 't' mode
# '+' open a disk file for updating (reading and writing).


# now we can read the number of characters in a file 
# f = open("demo.txt","r")
# data = f.read(4)
# print(data)
# f.close()

# we can also read text from the files line by line
f = open("uk.txt","r")
line1 = f.readline() # this is method for reading a line from the text
print(line1)

# for line2 reading
line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)


# now we write something on the first file and use the mode 'w'
f = open('demo.txt','w')
f.write('Appitech is a good company') # after that when you read it then it will show these text
f.close()
# # now open it again
# f = open('demo.txt','r')
# read_file = f.read()
# print(read_file) #Appitech is a good company

# f.close()

# here now we use the file 'a' mode 
# again i take text again
# f = open('demo.txt','a')
# update_file = f.write("\nHello this is appifytech company and working as a internee")
# f.close()

# f = open('demo.txt','r')
# file = f.read()
# print(file)


#  if file is not exist then we will create on this method
f = open("umair.txt","w")


# now we use 'r+'
f = open('demo.txt','r+')
f.write("Hell bro")  # f.write() returns the number of characters written, not a file object
f.seek(0)  # Move the file pointer back to the start to read from the beginning
print(f.read())  # Now you can read the updated content
f.close()
