
name = 'Ahmed  '  # string
##### operation on the string
#1- get length of the string
print(len(name))
# 2- access chars in the string using index--> index start from 0
# print(name[2])
# print(name[2:])
# print(name[2:4])
# print(name[::-1])
# name[3]='t' ##not allowed operation
## string is immutable ---> cannot be changed after creation.

# 3- string concat
# name ='noha'
# lname= 'shehab'
# name =name + lname
## 4- count no of occurence of chars in the string
iti = 'Information technology institute'
print(iti.count('i'))  # case sensetive

#5- convert string to upper , lower cases , title , capitalize
info = 'my name is Noha'
# print(info.upper())
# print(info.lower())
# print(info.capitalize())
# print(info.title())

#6- string interpolation

# fname = 'noha '
# midname = 'abdelhady '
# lname='shehab'
#
# # fullname= fname + midname +  midname + lname
# fullname= fname + midname*2 + lname
# print(fullname)

#7- format string

# temp = "My name is {0} I works at {1}"
# print(temp.format('Noha', 'ITI')) # temp.format ---> return new string
# print(temp.format("Ahmed", 'Redhat'))
# print(temp.format("Redhat", 'Ahmed'))

# temp = "My name is {employeename} I works at {employeecompany}"
# print(temp.format(employeename='noha', employeecompany='iti'))

# f-format string ---> format string according to the variables in the script

# name = 'Noha'
# email= 'noha@gmail.com'
# temp = f"my name is {name} , you can reach me at {email}."
# print(temp)

#8- ask user to enter string
# name = input("pleae enter your name: ")  # input function always returns with string
# print(type(name))
# age= input("please enter your age : ")
# print(type(age))
# temp = f"my name is {name} , {age}."
# print(temp)

#9- examine string content

# num1 = input("please enter num1 : ")  # string
# print(num1.isdigit())  # return true 00> if string contain positive numeric value
#
# num2 = input("please enter num2 : ")
# print(num2.isalpha()) # return true 00> if string contain a-z ---> no spaces

## calculator

# num1 = input("please enter num1 : ")
# num2 = input("please enter num2 : ")
# if num1.isdigit() and num2.isdigit():
#     res = int(num1) + int(num2)
# else:
#     print("you should enter valid number ")

# 10 -examine string content
#
# mystr= '                    '
# # if mystr:
# #     print("Hi")
# # else:
# #     print("bye")
# name = input("please enter your name : ")
# # print(f"my name is {name}.")
# if name.isspace():  # return true if the string contain spaces only
#     print("please enter valid name.")
# else:
#     print(f"my name is {name}.")
#
# print("noha".islower())


#11-you can iterate on the string -->
name ='Ahmed'

### for loop ---> loop over the string

# for char in name:
#     print(f"char = {char}")
#
#
#
# print('---')
#

# 12-  string replace
message = 'I love python o o o o '  ## replace o with @
newstring =message.replace('o', '@',3)
print(newstring) # return with new string

#13- strip
# message = input("--> please your message ---")
# print(f"#{message}#")
# # remove spaces from the begining and the end of the string
# print(f"#{message.strip()}#")  # strip ---> return new string ---> remove spaces from
# ## the begining and the end of the string
# print(f"#{message.lstrip()}#")  # strip ---> return new string ---> remove spaces from
# ## the begining of the string
#
# print(f"#{message.rstrip()}#")  # strip ---> return new string ---> remove spaces from
# ## the end of the string








#
# message = input("--> please your message ---")
# # print(f"%{message}%")
# # print(f"%{message.strip('n o')}%")
#
# print(message.replace(" ", ''))
#






y = 3.15 # float
z = 4 + 5j # complex
c = complex(4, 5)


a, b, c, d = 10, 66.66, 76.3, 100.54

# print(max(a,b,c,d))

print(round(b))


# noha ---> nh

# iti ---> 0 ,2


############### range ===>data type

# myrange = range(10) # range object ---> loop over it
#
# for item in myrange:
#     print(f"item = {item}")

# myrange = range(10) # range object ---> loop over it

for item in range(0,5,2):
    print(f"item = {item}")










