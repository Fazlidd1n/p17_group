# class A:
#     def __init__(self):
#         self.a = 2
#         self.b = 3
#
#
# obj = A()
# print(obj.a)
# print(obj.b)


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number
#         self._balance = balance
#
#     @property
#     def account_number(self):
#         return self._account_number
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @account_number.setter
#     def account_number(self, account_number):
#         self._account_number = account_number
#
#     @balance.setter
#     def balance(self, balance):
#         self._balance = balance
#
#     def transform(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print("Successfully transformed")
#         else:
#             print("invalid amount")
#
#     def withdraw(self, amount):
#         if 0 < amount < self._balance:
#             self._balance -= amount
#             print("Successfully withdrawn")
#         else:
#             print("Mablag' yetarli emas !")
#
#
# obj = BankAccount("5274", 50000)
# print("Balance :", obj.balance)
# obj.transform(10000)
# print("Balance :", obj.balance)
# obj.withdraw(30000)
# print("Balance :", obj.balance)


# class Student:
#     def __init__(self, student_id: int, first_name: str, last_name: str):
#         self._student_id = student_id
#         self._first_name = first_name
#         self._last_name = last_name
#         self._courses = []
#
#     def add_course(self, course:str):
#         self._courses.append(course)
#
#     def drop_course(self, course:str):
#         if course in self._courses:
#             self._courses.remove(course)
#             print(f"{course} - deleted")
#         else:
#             print("Not found course !")
#
#     def get_courses(self):
#         return self._courses
#
#     def get_fullname(self):
#         return f"Student : {self._first_name} {self._last_name}"
#
#     @property
#     def student_id(self):
#         return self._student_id
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @property
#     def last_name(self):
#         return self._last_name
#
#
# user = Student(1, "Fazliddin", "Ismoilov")
#
# print(user.get_fullname())
# user.add_course("Python")
# user.add_course("Java")
# user.add_course("C++")
# print(user.get_courses())
# user.drop_course("Java")
# print(user.student_id)


# class Car:
#     def __init__(self, company: str, model: str, year: int):
#         self._company = company
#         self._model = model
#         self._year = year
#         self._is_running = False
#
#     def start(self):
#         if self._is_running:
#             print("Car is already start ! \n")
#             return
#         self._is_running = True
#
#     def stop(self):
#         if self._is_running != True:
#             print("Car is already stop ! \n")
#             return
#         self._is_running = False
#
#     def is_running(self):
#         return self._is_running
#
#     def get_info(self):
#         return f"Company : {self._company} \nModel : {self._model} \nYear : {self._year} \nIs running : {self._is_running}"
#
#     @property
#     def company(self):
#         return self.company
#
#     @property
#     def model(self):
#         return self.model
#
#     @property
#     def year(self):
#         return self.year
#
#     @property
#     def is_running(self):
#         return self._is_running
#
#
# car1 = Car("BMW", "M5 Compition", 2022)
# print(car1.is_running)
# car1.start()
# # car1.stop()
# print(car1.get_info())


