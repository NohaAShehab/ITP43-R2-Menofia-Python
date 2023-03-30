# import modules_packages
#
# print(modules_packages.name)
# #
# modules_packages.sayhello('Ali')

""" alais the module """
""" import all the module in the script """
# import modules_packages  as testmodule
#
# print(testmodule.name)
# testmodule.sayhello('Noha')

""" import part of the module """
# from modules_packages import name , sayhello
# print(name)
#
# sayhello('6576')
# name = 'Ali'
# print(name)
""" import module from package """
# import systemadminpkg.greetings
#
# systemadminpkg.greetings.sayhello('Ahmed')

# import systemadminpkg.greetings as greet
#
# greet.sayhello('Ahmed')

"""import part of the module """
# from systemadminpkg.greetings import sayhello
#
# sayhello('Ahmed')
#
# from systemadminpkg.greetings import saywelcome as welcome
# welcome('Ali')

"""packages with __init__ file """
"""1- import package """
# import  iti
# iti.print_package_info()

# import  iti.helper
# num=iti.helper.askforInt()
# print(num, type(num))

# from iti.helper import askforInt
# num = askforInt()
# print(num, type(num))

#
# from iti import askforInt
# num = askforInt()
# print(num)


import  iti

iti.print_package_info()  # access package content using packagename only


import test
test.testpackage()






