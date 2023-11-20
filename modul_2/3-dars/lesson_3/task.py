class Student:
    def __init__(self, student_id , first_name , last_name):
        self._student_id = student_id
        self._first_name = first_name
        self._last_name = last_name
        self._courses = []

    @property
    def student_id(self):
        return self._student_id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def add_course(self , course):
        self._courses.append(course)

    def drop_course(self , course):
        if course in self._courses:
            self._courses.remove(course)
        else:
            print("Not found course !")

    def get_courses(self):
        return self._courses

    def get_fullname(self):
        return f"Student : {self.first_name} {self.last_name}"

student1  = Student(1 , "Botir" , "Qodirov")
student1.add_course("Java")
student1.add_course("Python")
student1.add_course("Foundation")
student1.drop_course("Java")
print(student1.get_courses())
print(student1.get_fullname())


