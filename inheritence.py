"""
    inheritance ===> inherit properties and methods
"""
# class Person:
#     pass
#
#
# class Employee(Person):
#     pass
#
#
# emp = Employee()
#
# print(isinstance(emp, Employee))
# print(isinstance(emp ,Person))
""" parent class with constructor """
# class Person:
#     def __init__(self,name):
#         self.name =name
#
#
# class Employee(Person):
#     pass
#
#
# emp = Employee("Ahmed")
""" child class with constructor """
# class Person:
#     def __init__(self,name):
#         self.name =name
#
#     def speak(self):
#         print(f'{self.name}')
#         print("I am a person")
#
#
# class Employee(Person):
#     def __init__(self, email):
#         self.email = email
#
#
# emp = Employee("Ahmed")
# emp.speak()

""" call parent constructor """
# class Person:
#     def __init__(self,name):
#         self.name =name
#
#     def speak(self):
#         print(f'{self.name}')
#         print("I am a person")


# class Employee(Person):
#     def __init__(self,username, email):
#         super().__init__(username)
#         super(Employee, self).__init__(username)
#         # Person.__init__(self, username)
#         self.email = email
#
#
#
# emp = Employee("Ahmed",'ahmed@gmail.com')
# emp.speak()
# print("------")

""" support multi-level inheritance """

#
# class Human():
#     def speak(self):
#         print("I am a human")
#
#
# class Employee(Human):
#     def __init__(self,name):
#         self.name= name
#
#
# class Engineer(Employee):
#     def __init__(self, salary):
#         super(Engineer, self).__init__(name='Ali')
#         self.salary=salary
#
#
# eng = Engineer(5446)
# eng.speak()
# print(isinstance(eng,Human))
# print(isinstance(eng, Employee))

""" multiple inheritance """

# class Teacher:
#     def speak(self):
#         print("I am a teacher")
#
# class Engineer:
#     def __init__(self,name):
#         self.name = name
#
#     def speak(self):
#         print("I am an engineer")
#
# class Instructor(Teacher, Engineer):
#     pass
#
# inn = Instructor("Ahmed")
# print(isinstance(inn, Teacher))
# print(isinstance(inn, Engineer))
# inn.speak()
""""""
# class Teacher:
#     def __init__(self, salary):
#         self.salary = salary
#
#
#     def speak(self):
#         print("I am a teacher")
#
# class Engineer:
#     def __init__(self,name):
#         self.name = name
#
#     def speak(self):
#         print("I am an engineer")
#
# class Instructor(Teacher, Engineer):
#     pass
#
# inn = Instructor("Ahmed")
# print(isinstance(inn, Teacher))
# print(isinstance(inn, Engineer))
# inn.speak()

""" Instructor with init function """
class Teacher:
    def __init__(self, salary):
        self.salary = salary


    def speak(self):
        print("I am a teacher")

class Engineer:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("I am an engineer")

class Instructor(Teacher, Engineer):
    def __init__(self,name, salary):
        super(Instructor, self).__init__(salary)
        Engineer.__init__(self, name)

inn = Instructor("Ahmed", 34325)
print(isinstance(inn, Teacher))
print(isinstance(inn, Engineer))
inn.speak()

























