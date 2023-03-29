""" list can hold different values from different datatypes

    you can access list elements using index ---> index start from zero
"""

""" 1- define a list """

l = []
myl= []
mixed_list = ["Ahmed", 'Ali', 2023, 3.14, True, None, "iti",'system admin', 'iti']

"""2- calculate length of the list """
print(len(mixed_list))

"""3- get element from the list using index --> index start from zero """
print(mixed_list[4])
# print(mixed_list[200])  # list index out of range
"""4-lists are mutable datatype --> """
mixed_list[4]= 'updated'
print(mixed_list)

"""5- append element to the list ? ===> add element at the end of the list """
mixed_list.append("noha")
print(mixed_list)
"""6- insert element at certain position -->at index ... """
mixed_list.insert(4, 'inserted')
print(mixed_list)
mixed_list.insert(100, 'myvalue')
print(mixed_list)

"""7- pop value from the list """
popped_element = mixed_list.pop()#remove the last element in the list and return with it .
print(popped_element)
print(mixed_list)

"""8- pop element at certain index """
popped_element = mixed_list.pop(4)
print(popped_element)
print(mixed_list)

"""9- remove element from the list """
# mixed_list.remove("iti")  # remove the first occurrence of the element
# print(mixed_list)

"""10- get index of element """
selected_index = mixed_list.index("iti")   # index ---> works also with string
print(selected_index)

"""11- loop over the list """
# for element in mixed_list:
#     print(f"element = {element}")

"""12-print index of each element in the list """
# counter= 0
# for element in mixed_list:
#     print(f"{counter} = {element}")
#     counter +=1

# print(enumerate(mixed_list))  # create index for the iterable
#
# for index , item in enumerate(mixed_list):
#     print(f"{index}->{item}")
# #
# for i , char in enumerate("noha"):
#     print(f"{i}---> {char}")
"""13- check if element exists in the list ?  """
# print('iti' in mixed_list)
# print("system_admin" in mixed_list)
# print('i' in ['i', 'e', 'o', 'u','a'])
# if 'n' in 'noha':
#     print("found")
# else:
#     print("not found")

"""14- list concatenation """

# l1 = ['admin1', 'python']
# l2 =['bash script', 'networks', 'cloud']
# system_admin_courses = l1 + l2  # return new list
# print(system_admin_courses)

"""15- extend a list --->"""
l1 = ['admin1', 'python', 'cloud']  #
l2 =['bash script', 'networks', 'cloud']
l1.extend(l2)  # extend l1 elements with l2 elements
print(l1)
print(l2)

"""16- sort the list ---> list elements must be from the same type """
## sort ---> depend on < , > --->
# print("ahmed"> 10 )
# names = ['ahmed', 'Mohamed', 'omar', 'dina', 'adel', 'mostafa']
# # names.sort() # sort elements in the list itself --> ascending
# # print(names)
# names.sort(reverse=True) # sort elements in the list itself --> ascending
# print(names)

""" 17-reverse a list ---> doesn't require list elements to be from the same type"""
print(mixed_list)
mixed_list.reverse()
print(mixed_list)


# l = list([5, 6, 7])


l1= [3,True, 44, 'Ahmed']
l2= ['python', 'redhat', 'iti', 2023, l1]
print(l2)

print(l2[4][3])

"""18- min and max """
l= [4,5,323,53,4,-19]
print(min(l))
print(max(l))

names= ['Ahmed', 'mohamed', 'ali', 'test']
print(min(names))
print(max(names))

"""19- empty lists are falsy value """
l = []
if l:
    print("hi")
else:
    print("bye")


"20- remove all elements from the list at one time"
mixed_list.clear()
print(mixed_list)


"""21- cast string to a list ? """
name = 'ahmed'
name = list(name)
print(name)

"""22- split string to a list """
message = 'nice to meet you'
message = message.split(" ")
print(message)

"""23- join list elements into one string  ---> list elements are all strings """
names =['ahmed', 'mohamed', 'ali', 'omar']
names = '_'.join(names)
print(names)