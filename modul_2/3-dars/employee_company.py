class Employee:
    def __init__(self, emp_id: int, first_name: str, last_name: str, salary: int):
        self._emp_id = emp_id
        self._first_name = first_name
        self._last_name = last_name
        self._salary = salary

    def get_emp_id(self):
        return self._emp_id

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary: int):
        self._salary = new_salary


class Company:
    def __init__(self, name: str):
        self._name = name
        self._employees: list[Employee] = []

    def hire_employee(self, employee):
        self._employees.append(employee)

    def fire_employee(self, emp_id: int):
        for employee in self._employees:
            if employee.get_emp_id() == emp_id:
                self._employees.remove(employee)
                return

    def list_employees(self):
        for employee in self._employees:
            print(f"Employee-ID: {employee.get_emp_id()}\n"
                  f"Name: {employee.get_full_name()}\n"
                  f"Salary: {employee.get_salary()}\n")


company = Company("FIDO Biznes")
emp1 = Employee(101, "Akbarali", "Salohiddinov", 3_000)
emp2 = Employee(102, "Asilbek", "Xolmatov", 3_000)
emp3 = Employee(103, "Iskandar", "Madaminjanov", 3_500)

# adding new employess to company
for employee in [emp1, emp2, emp3]:
    company.hire_employee(employee)

# print employees
company.list_employees()

# deleting employee
# id = int(input("employer id: "))
# check: str = input(f"Are you sure deleting? (Y/n): ")
# if len(check) == 1 and (check == "Y" or check == "y"):
#     company.fire_employee(id)
#     print("Succesfully deleted!")
# print("********************\n")

# print employees
company.list_employees()

# setting salary for employee
old_salary = emp1.get_salary()
emp1.set_salary(7_000)
new_salary = emp1.get_salary()
print(f"{emp1.get_full_name()}'s salary updated to {abs(old_salary-new_salary)}")
print("*********************\n")
