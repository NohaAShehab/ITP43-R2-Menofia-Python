
""" range """
#
# for i in  range(10):
#     print(f"i= {i}")

# myrange=  range(1,10,2)
# ## cast range to a list
# myl = list(myrange)
# print(myl)

# myrange=  range(100,10,-2)
# ## cast range to a list
# myl = list(myrange)
# print(myl)
################# loop ---> while loop ?

#known number of iterations --> for loop / while loop

## unknow number of iterations ---> while

# count = 0
# while count < 6:
#     print(count)
#     count += 1
# ##################################333
# for i in range(0,6):
#     print(i)

############# unknow number of iterations

# age = input("please enter age ")
# while not(age.isdigit()):
#     print("--- incorrect value for age ")
#     age = input("please enter your age: ")
#
# age = int(age)
# print(age)

""" break , continue ---> works with loops  """
# for i in range(10):
#     if i==4:
#         break
#     print(i)


# for i in range(10):
#     if i==4:
#         continue
#     print(i)

# count = 0
# while True:
#     if count==5:
#         break
#     print("Hello world")
#     count +=1
#
#




# while True:
#     age = input("please enter your age: ")
#     if age.isdigit():
#         break
#     else:
#         print("--- please enter correct value ")



# while True:
#     age = input("please enter your age: ")
#     if age.isdigit():
#         break
#
#     print("--- please enter correct value ")
######################################
#
#
# for i in range(10):
#     if i==4:
#         continue
#     print(f"i={i}")
#
#
# print("---- loop ended ----- ")





# for i in range(10):
#     if i==4:
#         break
#     print(f"i={i}")
#
#
# print("---- loop ended ----- ")



################33

# for i in range(10):
#     if i==4:
#         break
#     print(f"i={i}")
# else:
#     print("--- this block will be executed only if your loop reached its end .")
#     print("---- loop ended ----- ")

# for i in range(3):
#     password = input("please enter password: ")
#     if password=='123':
#         print("---logged_in successfully")
#         break
# else:
#     print("--- your account is disabled ")

######################### pass keyword
name=''


"""
    if(name=='ahmed'){}

"""
if name=='ahmed':
    pass

while True:
    pass  # null operation ---> when syntax requires a line to be added


print("-----")









