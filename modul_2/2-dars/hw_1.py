class Person:
    year = 2023

    def __init__(self, firstname: str, lastname: str, age: int, address: str):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.address = address

    def about_person(self):
        return f"Fullname: {self.firstname} {self.lastname}\nAge: {self.age}\nAddress: {self.address}"

    def birth_year(self):
        return f"{self.firstname}'s birthyear: {self.year - self.age}"


class Student(Person):
    def __init__(self, firstname: str, lastname: str, age: int, address: str):
        super().__init__(firstname, lastname, age, address)

    def course(self):
        return f"Now I'm studying at {self.age - 18}-course"


class Teacher(Person):
    def __init__(self, firstname: str, lastname: str, age: int, address: str):
        super().__init__(firstname, lastname, age, address)

    def subject(self, name_subject: str):
        self.name_subject = name_subject
        return f"{self.firstname} is teacher at {self.name_subject}-subject"


class Job(Person):
    def __init__(self, firstname: str, lastname: str, age: int, address: str):
        super().__init__(firstname, lastname, age, address)

    def type(self, job_type: str):
        self.job_type = job_type
        return f"{self.firstname} works as a {self.job_type}"


class Developer(Person):
    def __init__(self, firstname: str, lastname: str, age: int, address: str):
        super().__init__(firstname, lastname, age, address)

    def __str__(self):
        return f"Hi! I'm {self.firstname} {self.lastname}. I'm {self.age}-years old and now I'm working as Python Backend Developer in {self.address}"

    def company(self, name_company: str):
        self.name_company = name_company
        return f"{self.firstname} works at {self.name_company}"


p1 = Teacher("Akbarali", "Salohiddinov", 20, "Tashkent")
p2 = Developer("Botirjon", "Qodiraliyev", 25, "Yunusobod-7, 27-dom, 56-uy")
# print(p1)
print(p1.about_person())
print(p1.birth_year())
print(p1.subject("Math"))
# print(p2)
print(p2.company("PDP Academy"))

