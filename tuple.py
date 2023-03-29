""" tuple can hold different values from different datatypes

    you can access tuple elements using index ---> index start from zero
"""

""" 1- define a tuple """

l = ()
myl= tuple()
mixed_tuple = ("Ahmed", 'Ali', 2023, 3.14, True, None, "iti",'system admin', 'iti')

"""2- calculate length of the tuple """
print(len(mixed_tuple))
#
"""3- get element from the tuple using index --> index start from zero """
print(mixed_tuple[4])
# print(mixed_tuple[200])  # tuple index out of range
"""4-tuples are immutable datatype --> """
# mixed_tuple[4]= 'updated'  # 'tuple' object does not support item assignment
# print(mixed_tuple)
#






"""5- get index of element """
selected_index = mixed_tuple.index("iti")   # index ---> works also with string
print(selected_index)
#
"""6- loop over the tuple """
for element in mixed_tuple:
    print(f"element = {element}")

"""7-print index of each element in the tuple """
counter= 0
for element in mixed_tuple:
    print(f"{counter} = {element}")
    counter +=1
#
# # print(enumerate(mixed_tuple))  # create index for the iterable
# #
for index , item in enumerate(mixed_tuple):
    print(f"{index}->{item}")
#

"""8- check if element exists in the tuple ?  """
print('iti' in mixed_tuple)
# # print("system_admin" in mixed_tuple)

#
"""9- tuple concatenation """
#
t1 = ('admin1', 'python')
t2 =('bash script', 'networks', 'cloud')
system_admin_courses = t1 + t2  # return new tuple
print(system_admin_courses)






#
t1= (3,True, 44, 'Ahmed')
t2= ('python', 'redhat', 'iti', 2023, t1, [23,546,54])
# print(t2)
#
# print(t2[4][3])
# print(t2[5])
#
# t2[5].append("inseeted element")
#
"""18- min and max --> items must be from  the same datatypes  """
t= (4,5,323,53,4,-19)
print(min(t))
print(max(t))
#
# names= ['Ahmed', 'mohamed', 'ali', 'test']
# print(min(names))
# print(max(names))
#
"""19- empty tuples are falsy value """
t = ()
if t:
    print("hi")
else:
    print("bye")


#
"""21- cast string to a tuple ? """
name = 'ahmed'
name = tuple(name)
print(name)
#

# """23- join tuple elements into one string  ---> tuple elements are all strings """
names =('ahmed', 'mohamed', 'ali', 'omar')
names = '_'.join(names)
print(names)

""" tuple of one element """
myt = ('noha',)  #
print(myt, type(myt))

"""cast tuple to a list and vice versa ? """

t = ('iti',2023, 'Menofia', 'python')
t =  list(t)
print(t, type(t))