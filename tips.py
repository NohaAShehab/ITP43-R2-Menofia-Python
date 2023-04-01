
# l = [35,56,7,4,43]
# a,*b,*c=l

# with open("inheritence.py", 'r') as fileobj:
#     print(fileobj.read())

""" list comprehsion"""

""" generate list of even numbers ---> number in range 1 , 100 """

# nums = range(0,101, 2)
# print(list(nums))

# nums = [ x for x  in range(11) if x%2==0]
# print(nums)
# nums = [ x*x for x  in range(11) if x%2==0]
# print(nums)
#
# l =['0','tt',23,45]
# print(all(l))
# print(any(l))
"lambda"
# def add_four(num):
#     return num+4

# anfun =lambda num1, num2: (num1+4)*num2
# print(anfun(45,4))

"""map , filter """

l = [2,4,67,83,757,78,34,3,323]

# def multiply_by_five(l):
#     for  index, item in enumerate(l):
#         l[index] = item*5
#
#     return l
#
# print(multiply_by_five(l))

# l = map(lambda item:item*5, l)  # map object ---> casted to a list
# print(l)
# l = list(l)
# print(l)

l = [2,4,67,83,757,78,34,3,323]
# """ filer odd number """
# l = filter(lambda x:x%2!=0 , l)  #filter object
# print(l)
# print(list(l))


" function return a function "


def saywelcome():
    print("welcome to python")
    name ='Ahmed'
    return lambda message: print(message+name)

res = saywelcome()

print("00000000000000000000")
res('iroieoi')
# # res('Hello world')

# # print("----------------")
# saywelcome()('Python is easy')




class pythonQueue:
    pass


class MyException(Exception):
    pass
name=input("please enter name: ")
if not name:
    raise MyException("test")