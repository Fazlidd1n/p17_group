# Employee(emp_id: int, first_name: str, last_name: str, salary: int)
#         def : get_emp_id , get_full_name , get_salary , set_salary
#
#     Company(name: str , employees : list[Employee])
#         def : hire_employee , fire_employee , list_employees


class Employee:
    def __init__(self, emp_id: int, firstname: str, lastname: str, salary: int):
        self._emp_id = emp_id
        self._firstname = firstname
        self._lastname = lastname
        self._salary = salary

    @property
    def emp_id(self):
        return self._emp_id

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def salary(self):
        return self._salary

    def get_fullname(self):
        return f"{self._firstname} {self._lastname}"

    def set_salary(self, new_salary):
        self._salary = new_salary


class Company:
    def __init__(self, name: str):
        self._name = name
        self._list_employees: list[Employee] = []

    def hire_employee(self, employee: Employee):
        self._list_employees.append(employee)
        print("Successfuly add employee !")

    def fire_employee(self, employee: Employee):
        if employee in self._list_employees:
            self._list_employees.remove(employee)
            print("Successfuly delete employee !")

    def list_employees(self):
        return self._list_employees


emp1 = Employee(1, "Fazliddin", "Ismoilov", 2_000_000)
emp2 = Employee(2, "Suxrop", "Botirov", 1_500_000)
pdp = Company("Pdp Academy")
pdp.hire_employee(emp1)
pdp.hire_employee(emp2)
print(emp1.get_fullname())
for i in pdp.list_employees():
    txt = f"""
id = {i.emp_id}
first name = {i.firstname}
lastname = {i.lastname}
salary = {i.salary}"""
    print(txt)
