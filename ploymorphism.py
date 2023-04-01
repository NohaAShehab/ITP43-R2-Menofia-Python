"""
        polymorphism
        ---> overriding


        ---> overloading
"""
# class Human:
#
#     def speak(self):
#         print("---- I am human ")
#
# class Employee(Human):
#     pass
#
# emp = Employee()
# emp.speak()


""" overriding """
""" 2 classes ---> have inheritance relation --->
have the same method name  --> different implementation --> override 
"""
# class Human:
#     def speak(self):
#         print("---- I am human ")
#
# class Employee(Human):
#     def speak(self):
#         print("I am an employee")
#
# class Instructor(Human):
#     def speak(self):
#         print("I am an Instructor")
#
# emp = Employee()
# emp.speak()
#
# inn= Instructor()
# inn.speak()

""""""
# class Human:
#     def speak(self):
#         print("---- I am human ")
#
# class Employee(Human):
#     def speak(self):
#         super().speak()
#         print("I am an employee")
#
# class Instructor(Human):
#     def speak(self):
#         print("I am an Instructor")
#
# emp = Employee()
# emp.speak()
#
# inn= Instructor()
# inn.speak()

""" overload """

""" overloading --> 2 function in the same class with same ---> different in no of paramers or 
type of parameters or both """
# class Human:
#     # def speak(self):
#     #     print("---- I am human ")
#
#     def speak(self, name:str , age:int):
#         print(f"I am human, {name}, {age}")
#
# h = Human()
# # h.speak()
# h.speak('Ahmed', 93)
# # h.speak()
#
#
#



class Human:
    # def speak(self):
    #     print("---- I am human ")

    def speak(self, name=None , age=None):
        print(f"I am human, {name}, {age}")
        if(isinstance(name, str) and( isinstance(age, int) and age!=0)):
            print("testttttttttttt")



h = Human()
h.speak()
h.speak('Ahmed', 93)
# # h.speak()
































