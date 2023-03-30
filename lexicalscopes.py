""" lexical scope """
# name= 'Ahmed'
#
# """ when you define variable inside the function --> this variable can be called only
# inside the function """
# def askforInt():
#     """ any variable is define inside the function ---> its scope local scope """
#     num = input("please enter num: ")  # local scope
#     print(num)
#     return  num  # return with value
#
# res= askforInt()
# print(name)

###################################################################
# num = 10
#
# def printnum():
#     num = input("please enter number : ")  # local variable ---> in the function
#     print(num)
#
#
# printnum()
# print(num)

#################################
""" any variable defined in the script outside the function
variable can be accessed anywhere in the script -->you print(read value )---> in the function

"""
# num = 10  # global
# def printnum():
#     print(f"num= {num}") # access from the function.
#
# printnum()

###############3
# num = 10  # global
# def printnum():
#     num = 'test'
#     print(f"num= {num}") # access from the function.
#
# printnum()
##############################
""" modify the global variable from inside the function """
# num= 10
# def modifynum():
#     global num
#     num = 'test'
#     print(f"num= {num}") # access from the function.
#
# modifynum()
# print(num)

#####################################################
"""python support ---> create function inside a funtion """

# def outerfunction():
#     name ='Ahmed'
#     print(name)
#
#     def innerfunction():
#         print("====Hello from the inner function ====")
#
#     innerfunction()
#
#
# outerfunction()

""" """
#
# def outerfunction():
#     """ local variable can be accessed anywhere in the function even inside the inner function"""
#     name ='Ahmed'  # local variable
#
#
#     def innerfunction():
#         print("====Hello from the inner function ====")
#         print(name)
#         print("==========================")
#
#     innerfunction()
#     print(name)
#
# outerfunction()
#
#
#
#
#
#
#
#
#
#
#
#

""" modify the local variable from innerfuntion  """

# def outerfunction():
#     """ local variable can be accessed anywhere in the function even inside the inner function"""
#     name ='Ahmed'  # local variable
#
#
#     def modifyname():
#         print("====Hello from the inner function ====")
#         name= 'noha'  # create new local variable for the modifyname function
#         print(name)
#         print("==========================")
#
#     modifyname()
#     print(name)
#
# outerfunction()
''
# def outerfunction():
#     """ local variable can be accessed anywhere in the function even inside the inner function"""
#     name ='Ahmed'  # local variable
#     def modifyname():
#         nonlocal name  # don't create new local variable use the own in the parent scope
#         print("====Hello from the inner function ====")
#         name= 'noha'
#         print(name)
#         print("==========================")
#
#     modifyname()
#     print(name)
#
# outerfunction()
""" call global variable from inner function """
# track  ='system admin '
# def outerfunction():
#     name ='Ahmed'  # local variable
#     def modifyname():
#         nonlocal name
#         print("====Hello from the inner function ====")
#         print(track)
#         name= 'noha'
#         print(name)
#         print("==========================")
#
#     modifyname()
#     print(name)
#
# outerfunction()
""" modify global variable from  inner function ? """

track  ='system admin'
def outerfunction():
    name ='Ahmed'  # local variable
    def modifyname():
        global track
        nonlocal name
        print("====Hello from the inner function ====")
        track="System Adminstration"
        print(track)
        name= 'noha'
        print(name)
        print("==========================")

    modifyname()
    print(name)
    print(f"=== after the inner function {track}")

outerfunction()


print(f"after the function {track}")






























