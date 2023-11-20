# N1
from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int | str):
        self.name = name
        self.age = age

    def introduce(self):
        pass


class Customer(Person):

    def __init__(self, name: str, age: int | str, customer_id: int):
        super().__init__(name, age)
        self.customer_id = customer_id

    def purchase(self):
        pass


class Manager(Person):

    def __init__(self, name: str, age: int | str, department: str):
        super().__init__(name, age)
        self.department = department

    def manage(self):
        pass

    def display_salary(self):
        pass


class Developer(Person):

    def __init__(self, name: str, age: int | str, programming_language: str):
        super().__init__(name, age)
        self.programming_language = programming_language

    def code(self):
        pass
