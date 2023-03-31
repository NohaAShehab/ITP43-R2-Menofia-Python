# import  os
#
#
# print(os.getcwd())  # print the path I am in
#
# print(os.getlogin())
#
# # print(os.system('mkdir test'))
#
# print(os.system('ls -l'))





# import  math
# print(math.pi)
#
# print(math.pow(3,5))
#
# print(math.ceil(45.2))
#
# print(math.floor(45.2))
#####################################################

import re

# email= input("please enter your email: ")

# if '.'in email and '@' in email:
#     print("email valid")
# else:
#     print('email not valid')

####
email= input("please enter your email: ")

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# res = re.match(pattern, email)  # if email match pattern --> match object
# """ match function return with match object if part of the string match the pattern"""
# print(res)
#
# if res:
#     print("--email correct--")
# else:
#     print("-- email not correct ---")




# res = re.fullmatch(pattern, email)  # if email match pattern --> match object
# """ fullmatch function return with match object if all string match the pattern"""
# print(res)
#
# if res:
#     print("--email correct--")
# else:
#     print("-- email not correct ---")

#
#
#
# res = re.search(pattern, email)
# """ fullmatch function return with match object if all string match the pattern"""
# print(res)
# #
# # if res:
# #     print("--email correct--")
# # else:
# #     print("-- email not correct ---")












