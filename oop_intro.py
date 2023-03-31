

# l = [34,56,567,4]
# print(len(l))
# l.append('344')


# emp = {
#     "name":"Ahmed",
#     "salary":1000,
#     "dept":"system admin"
# }
#
# print(emp)
# emp2 = {
#     "emp_name":"Ali",
#     "salary":1000,
#     "dept":"system admin"
# }

"""
    class ---> define structure --> properties , functionality
    --> define your own datatype
"""
# class Employee:
#     pass
#
#
# e =  Employee()  # object ., object
# print(e)
#
# print(isinstance(e, Employee))
#######################################################3
"""take instance from class """
# class Employee:
#     pass
# e =  Employee()  # object ., object
# print(e)
#
# e.name='Ahmed'
# e.email='ahmed@gmail.com'
#
# print(e.name)
# e.name='ali'
#
#
# e2 = Employee()
# e2.city= 'Cairo'
# e2.salay = 1000


##############################################
"""create constructor ---> __init__ function (initialization function)"""

# class Employee:
#     def __init__(self):
#         print("==== init function is begin called -- while creating the object ")
#         print(self)
#
# emp1 = Employee()  # when create new object --> the __init__ function will be called
# print(emp1)

""" ask constructor to populate the object with data """
# class Employee:
#     def __init__(self):
#         self.name= 'Ahmed'
#         self.salary = 1000
#
#
# emp = Employee()
# emp.name ='test'
# emp2 = Employee()
""" customize object creation """
#
# class Employee:
#     def __init__(self, empname, salary):
#         self.name= empname
#         self.salary = salary
#
#
# emp = Employee("Ahmed", 1000)
# emp.name = 'Abanoub'
# emp.city = 'Cairo'
# emp2= Employee('Ali', 24235)
""" constructor with default params """



# class Employee:
#     def __init__(self, empname, salary=1000):
#         ### instance varibales
#         self.name= empname   #object ==> instance
#         self.salary = salary
#         ## name , salary ==> instance variables
#
#     #instance method
#     def speak(iti):
#         print(iti.name)
#         # print(f"I am an Employee, my name is {self.name}, {self.salary}")
#         print("03490")
#
#     def saymessage(self, message):
#         print(f"{message}")
#
#
#
# emp = Employee("Ahmed")
# emp.speak()
#
# emp2= Employee('soliman', 342550)
# emp2.speak()
# emp2.saymessage('Nice to meet you ...')

""" -----> count number of objects created from the class """
""" """
# class Employee:
#     count =0    # class variable -> variable represent class property --> values
#     # # represent class itself not the instance
#
#     def __init__(self, empname, salary=1000):  # init ---> object
#         self.name= empname
#         self.salary = salary
#         Employee.count +=1
#
#
#
#     def saymessage(self, message):
#         print(f"{message}")
#
#
#
# emp1 = Employee("test", 938089)
# emp2= Employee('soliman', 342550)
# emp2.saymessage('Nice to meet you ...')
# print(Employee.count)
#
# Employee.count =10
#
# emp1.count =-3
#
# # Employee.count = 100



""" class method """

# class Employee:
#     count =0
#
#     def __init__(self, empname, salary=1000):  # init ---> object
#         self.name= empname
#         self.salary = salary
#         Employee.count +=1
#
#     def saymessage(self, message):
#         print(f"{message}")
#
#     """ function represent behaviour related to the class --> cls --> represent class """
#     @classmethod
#     def get_no_of_employees(cls):
#         print(cls)
#         print(cls.count)
#
#     @classmethod  # object factory ? ---> return new object from the class
#     def create_Emp(cls):
#         e=cls("default", 0)
#         return e
#
#
# emp1 = Employee("test", 938089)
# emp2= Employee('soliman', 342550)
# Employee.get_no_of_employees()
# print(Employee.count)
# emp3 = Employee.create_Emp()
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
#
#
#
#
""" ============> Static method <=============="""

class Employee:
    count =0

    def __init__(self, empname, salary=1000, location='cairo'):  # init ---> object
        self.name= empname
        self.salary = salary
        Employee.count +=1
        self.location =location

    def saymessage(self, message):
        print(f"{message}")

    @classmethod
    def get_no_of_employees(cls):
        print(cls)
        print(cls.count)

    @classmethod  # object factory ? ---> return new object from the class
    def create_Emp(cls):
        e=cls("default", 0)
        return e


    """static methods are helper methods ---> 
    behaviour --> doesn't depend on the class or on the object"""
    @staticmethod
    def cal_net_cal(salary):
        return salary * .8


    @staticmethod
    def prepare_String(anystring):
        return anystring.strip()






emp1 = Employee("      test", 938089)
emp2= Employee('soliman', 342550)

print(Employee.prepare_String(emp1.name))
# def cal_net_cal(salary):
#     return salary*.8
#
#
# print(cal_net_cal(emp1.salary))
# print(cal_net_cal(100000))


print(Employee.cal_net_cal(emp1.salary))
print(Employee.cal_net_cal(89274897))



""" you represent object properties in form of dict """

print(emp1.__dict__)
emp2.saymessage('ejkwrhjkqwr')





























