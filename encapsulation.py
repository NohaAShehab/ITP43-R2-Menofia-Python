"""

    access modifiers

    public --> variable/ method ---> can be accessed anywhere in the scripts
    protected -->variable/ method ---> can be accessed anywhere in the class or in the derived classes
    private -->variable/ method ---> can be accessed only in the class

    'in python --> No access modifiers'

    define name of variable or function
    starts with
        [a-z] ==> public
        _ ==> protected
        __ ==> private


"""
#
# class Employee:
#     def __init__(self,name, age, salary):
#         self.name = name
#         self._age = age    # protected
#         self.__salary = salary
#
#     def test(self, email):
#         self.__email = email
#
#     def display_emp_info(self):
#         print(f"My name is {self.name}, my salary = {self.__salary}")
#
# emp= Employee('Noha', 24, 90248)
# print(emp.name)
# print(emp._age)  # ethically don't do that
# # print(emp.__salary) ### inside class
# # print(emp._Employee__salary)  # scope binding  ---> please don't do this
# emp.display_emp_info()
#
#
#
#
# class Engineer(Employee):
#     def speak(self):
#         print(f"{self.name}, {self._age}, {self.__salary}")  # raise error
#
# eng = Engineer('Ahmed',23,2394)
# eng.speak()


##############################################
""" I need to access private members 
    limit accessibility to the properties 
    --> private ---> I need to apply constraint on setting and getting the value 
"""

# class Employee:
#     def __init__(self,name, age, salary):
#         self.name = name
#         self._age = age    # protected
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary*.8
#
#     def set_salary(self, sal):
#         if isinstance(sal, float) or isinstance(sal, int) and sal > 0:
#             self.__salary = sal
#         else:
#             raise ValueError("Salary should float number and > 0")
#
#     def display_emp_info(self):
#         print(f"My name is {self.name}, my salary = {self.__salary}")
#
#
#
# emp = Employee('noha',39,28937)
# print(emp.get_salary())
# emp.set_salary(423)

"""still we have a problem """
# class Employee:
#     def __init__(self,name, age, salary):
#         self.name = name
#         self._age = age    # protected
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary*.8
#
#     def set_salary(self, sal):
#         if isinstance(sal, float) or isinstance(sal, int) and sal > 0:
#             self.__salary = sal
#         else:
#             raise ValueError("Salary should float number and > 0")
#
#     def display_emp_info(self):
#         print(f"My name is {self.name}, my salary = {self.__salary}")
#
#
#
# emp = Employee('noha',39,'test')
# print(emp.get_salary())




""" to solve the problem """

# class Employee:
#     def __init__(self,name, age, salary):
#         self.name = name
#         self._age = age    # protected
#         self.set_salary(salary)
#
#     def get_salary(self):
#         return self.__salary*.8
#
#     def set_salary(self, sal):
#         if isinstance(sal, float) or isinstance(sal, int) and sal > 0:
#             self.__salary = sal
#         else:
#             raise ValueError("Salary should float number and > 0")
#
#     def display_emp_info(self):
#         print(f"My name is {self.name}, my salary = {self.__salary}")
#
#
#
# # emp = Employee('noha',39,'test')
# # print(emp.get_salary())
# emp = Employee('noha',39,657)
# emp.set_salary('ioeru')
# emp.name= 'jkshf'

"""property decorator """

# class Employee:
#     def __init__(self,name, age, salary):
#         self.name = name
#         self._age = age    # protected
#         # self.set_salary(salary)
#         # self.salary = salary
#         self.__salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary*.8
#
#     @salary.setter
#     def salary(self, sal):
#         if isinstance(sal, float) or isinstance(sal, int) and sal > 0:
#             self.__salary = sal
#         else:
#             raise ValueError("Salary should float number and > 0")
#
#     def display_emp_info(self):
#         print(f"My name is {self.name}, my salary = {self.__salary}")
#
#
#
# # emp = Employee('noha',39,'test')
# # print(emp.get_salary())
# emp = Employee('noha',39,1000)
# print(emp.salary)
# # emp.set_salary(938534)
# emp.salary= 100000





# class Employee:
#     def __init__(self,name, age, salary):
#         self.name = name
#         self._age = age    # protected
#         # self.set_salary(salary)
#         # self.salary = salary
#         # self.__salary = salary
#         self.salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary*.8
#
#     @salary.setter
#     def salary(self, sal):
#         if isinstance(sal, float) or isinstance(sal, int) and sal > 0:
#             self.__salary = sal
#         else:
#             raise ValueError("Salary should float number and > 0")
#
#     def display_emp_info(self):
#         print(f"My name is {self.name}, my salary = {self.__salary}")
#
#
#
# # emp = Employee('noha',39,'test')
# # print(emp.get_salary())
# emp = Employee('ali',23,70000)
# print(emp.salary)
# print('-------------------')

""" naming """


class Employee:
    def __init__(self,name, age, salary):
        self.name = name
        self._age = age    # protected
        self.salary = salary

    @property
    def age_after_10_years(self):
        return self._age + 10

    @property
    def salary(self):
        return self.__salary*.8

    @salary.setter
    def salary(self, sal):
        if isinstance(sal, float) or isinstance(sal, int) and sal > 0:
            self.__salary = sal
        else:
            raise ValueError("Salary should float number and > 0")

    def display_emp_info(self):
        print(f"My name is {self.name}, my salary = {self.__salary}")



# emp = Employee('noha',39,'test')
# print(emp.get_salary())
emp = Employee('ali',23,70000)
# print(emp.salary)
print('-------------------')



print(isinstance(emp, object))
# l = []
# l.append('errt')



























