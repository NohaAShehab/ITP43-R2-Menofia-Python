

# def get_full_name(firstname, lastname):
#     fullname = f"{firstname} {lastname}"
#     return firstname , fullname   # return --> in form of tuple --->
#
#
# myfullname = get_full_name("Ahmed", 'Mohamed')  #immutable
# print(myfullname)  ##

##########################################
""" functions with default arguments """
# def get_full_name(firstname, lastname='Ahmed'):
#     print(f"firstname={firstname}, lastname={lastname}")
#
#     fullname = f"{firstname} {lastname}"
#     return firstname , fullname
#
# get_full_name('Noha')
# get_full_name('Noha', 'Shehab')
#
# print("Hello", end='#')
# print("world")
#
# print("Ahmed", 'Mohamed', 'Ali',  sep='__||__')


# def get_full_name( lastname='Ahmed', firstname):  ### syntax error
#     print(f"firstname={firstname}, lastname={lastname}")
#
#     fullname = f"{firstname} {lastname}"
#     return firstname , fullname
#
# get_full_name('Ahmed', 'Mohamed')

########################################################
""" function that accepts variable number of arguments """
""" * ==> when call the function you can pass zero or more arguments """
# def ask_for_students_name(*students):  # all user to enter any number of argument zero or more
#     print(students) # tuple
#
#
# ask_for_students_name('Ahmed', 'Mohamed')
# ask_for_students_name()
# ask_for_students_name('Ahmed', 'Mohamed', 'Ali', True,9834)
#
# print()
# print("4535")
# print("Ahmed", 'Mohamed', 'Ali')
# print(4,45)

####################################################################

""" functions with keyword arguments """
def introduceyourself(**info):  #--> this function accept keyword --->
    print(info)


introduceyourself(name='noha', works='iti', study='cs')
introduceyourself(firstname='ahmed', lastname='mohamed', age=25)
introduceyourself()
introduceyourself(lname='ali')



############################################

# temp = "My name is {username}, I lives in {city}"
#
# print(temp.format(city='cairo', username='Ahmed'))


# temp = "My name is {0}, I lives in {1}"
#
# print(temp.format('cairo', 'Ahmed'))












