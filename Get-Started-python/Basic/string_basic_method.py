# first method is replace method that will convert the substring to another substring



string = "umairkhan"
old = "umair"
new = "saqib"
newstring = string.replace(old,new)
print(newstring)
print(string)


# split method
new_name = "University,of,Science,and,Technology,Bannu"
new_name2 = new_name.split(",")
print(new_name2)

# new string
city = "Newyork=USA=Dubai=Pakistan"
cityupdate = city.split('=')
print(cityupdate)

# join method
name = ('hello','umair','appify')
print(type(name)) # this is a tuple
# we make a one string from that
onestr = ' '.join(name)
print(onestr) # hello umair appify