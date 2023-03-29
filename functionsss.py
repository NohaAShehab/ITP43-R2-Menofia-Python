

# "1- to define  a function "
# def myfunction():
#     pass
#
#
# "2- call the function"
# myfunction()
# myfunction()

"3- check the function  ---> function  alaways returns with None, unless you say something else"
# def myfunction():
#     pass
#
# x= myfunction()
# print(x)

""
# def myfunction():
#     print("--- function is being executed ")
#     print("Hello world")
#
# x= myfunction()
# # print(x)
#
# y= myfunction()
# # print(y)



# def myfunction():
#     print("--- function is being executed ")
#     print("Hello world")
#     return
#
# x= myfunction()
# print(x)
# print("----------------------------------")
# y= myfunction()
# print(y)
############## function take arguments
# def sumnum(num1, num2):
#     res = num1 + num2
#     print(res)
#     print("---------------")
#     return res
#
#
# s = sumnum(1,4)
# m = sumnum(10,34)
# n = sumnum('10', '20')
# ss = sumnum(35,'34')

######################
'restrict datatype of variable'
# def sumnum(num1:int, num2:int) -> int :
#     print(f"num1= {num1}, num2= {num2}")
#     res = num1 + num2
#     print(res)
#     print("---------------")
#     return res
#
# r = sumnum(2,45)
#
# mm = sumnum("24","46")
#############################


# # python loosely dynamically typed lang. ---> interpreter detect datatype of variable in the runtime
# def sumnum(num1:int, num2:int) -> int :
#     print(f"num1= {num1}, num2= {num2}")
#     res = int(num1) + int(num2)
#     print(res)
#     print("---------------")
#     return res

# r = sumnum(2,45)
#
# mm = sumnum("24","46")
#
# dd= sumnum('5','ig')
#


print(isinstance('44', int))

# def sumnum(num1:int, num2:int) -> int :
#     ## check type of variable
#     if isinstance(num1, int) and isinstance(num2, int):
#         res =  num1 + num2
#         return res
#     else:
#         print("num1 and num2 should be integers")
#
#
# m =sumnum(10,30)
#
# n = sumnum('ahmed', 'test')

########################
""" isdigit ----> with string """
num = '434'
print(isinstance(num, str))  # check if variable ---> from the given datatype
print(num.isdigit()) # check if the string --> contains numeric value .



# def sumnum(num1, num2) :
#     ## check type of variable
#     if isinstance(num1, int) and isinstance(num2, int):
#         res =  num1 + num2
#         return res
#     else:
#         print("num1 and num2 should be integers")



"""
    myfun(4,5)
    [5,6,7,8]
"""

'abdulrahmanxyz'
"""
    abdu
    lr
    ahm
    anxyz
"""

















