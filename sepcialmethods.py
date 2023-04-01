

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age =age
#         self.__salary = salary
#
#     def __str__(self):
#         # print("---this function will be called when you try to print the object ")
#         return f"{self.name}"
#
# emp = Employee("Ahmed",23, 38989357)
# print(emp)
# emp2 = Employee("Ali",23, 38989357)
# print(emp2)



# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age =age
#         self.__salary = salary
#
#     def __repr__(self):
#         return f"Employee(name={self.name}, _age={self._age}, __salary={self.__salary})"
#
# emp = Employee("Ahmed",23, 38989357)
# print(emp)
# emp2 = Employee("Ali",23, 38989357)
# print(emp2)



""" call """



# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age =age
#         self.__salary = salary
#
#     def __str__(self):
#         return f'{self.name}'
#     def __repr__(self):
#         return f"Employee(name={self.name}, _age={self._age}, __salary={self.__salary})"
#
#     def __call__(self, *args, **kwargs):
#         print('Employee object is being called ')
#
# emp = Employee("Ahmed",23, 38989357)
# print(emp)
# emp2 = Employee("Ali",23, 38989357)
# print(emp2)
#
# emp2()
# emp()

""" list """
# l = [45,657,67]
# print(len(l))

class Employee:
    __objectss = []
    count= 0
    def __init__(self, name, age, salary):
        self.name = name
        self._age =age
        self.__salary = salary
        Employee.count +=1
        self.id = Employee.count
        Employee.__objectss.append(self)

    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f"Employee(name={self.name}, _age={self._age}, __salary={self.__salary})"

    def __call__(self, *args, **kwargs):
        print('Employee object is being called ')

    def __len__(self):
        return len(self.__dict__)

    @classmethod
    def get_all_object(cls):
        return cls.__objectss

# emp = Employee("Ahmed",23, 38989357)
# emp2 = Employee("Ali",23, 38989357)
#
# print(len(emp))
# print(len(emp.__dict__))
# print(Employee.get_all_object())



# def getnumbers(*nums):
#     print(nums)
#
# getnumbers()
# getnumbers(3)
# getnumbers(3,56,566,76)

def info(**myinfo):
    print(myinfo)


info(name='noha',work='iti')
info(fname='adel', lname='Eid')
info()

