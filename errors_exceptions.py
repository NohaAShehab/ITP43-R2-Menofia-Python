""" syntax error  ===> must be solved """

"logical error ?"
#
# def sumnum(num1, num2):
#     res = num1 * num2
#     print(res)
#
# sumnum(2,2)
# sumnum(2,3)

"""run time error / exception --> error cause application to stop  """
# print(name)
# print("=========================")
# print(1/0)

########################################################################
print("-------------------------------------")

# try:
#     print(name)
# except :
#     print("---- problem happened")
# #
# print("---- after this block ---")
######################################################
# try:
#     num = int(input("please enter number: "))
#     print(num)
# except:
#     print("--- problem happened")


""" see information about the problem """
# try:
#     num = int(input("please enter number: "))
#     print(num)
#     # print(10/0)
#     # print(name)
# except Exception as e :
#     print(f"--- problem happened {e}")

# zerodivisonerror
# valueError
# nameError

# try:
#     # print(name)
#     # print(5/0)
#     res= 5/0
# except NameError as ne:
#     print(ne)
#     name ='e'
# except ZeroDivisionError as ze:
#     print(f"===> {ze}")
#     res = 0
# except Exception as e:
#     print(f"---> {e}")
#
#
# print(res)


##########################################################
""" try , except ---> mandatory blocks  ---> else: optional """
# try:
#     num = int(input("please enter num: "))
# except Exception as e:
#     print(e)
#     num=0
# else:
#     """ this block will be executed if there is no problem """
#     print("===no problem happened ")
#     print(num, type(num))


# try:
#     num = int(input("please enter num: "))
# except Exception as e:
#     print(e)
#     num=0
# else:
#     """ this block will be executed if there is no problem """
#     print("===no problem happened ")
#     print(num, type(num))
# finally:
#     print("----------end of this part -------------------")
#     print("--- this block will be executed always ---")
# #


#
# try:
#     num = int(input("please enter num: "))
# except Exception as e:
#     print(e)
#     num=0
# finally:
#     print("----------end of this part -------------------")
#     print("--- this block will be executed always ---")

"######################### Raising Error ###################"

def divnums():
    num1 = input("please enter num1: ")
    num2 =input("please enter num2: ")  # "0"
    if num2=='0':
        raise ZeroDivisionError("---> cannot divide by zero ----")
    if num1.isdigit():
        num1 = int(num1)
    if num2.isdigit():
        num2 = int(num2)

    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 / num2
        return res
#
#
x = divnums()
