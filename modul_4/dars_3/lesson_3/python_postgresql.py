# import psycopg2
#
# # pip install psycopg2-binary
#
#
# query = """
#     select * from courses where id = %s;
# """
#
#
# class DB:
#     con = psycopg2.connect(database="lesson_3",
#                            user="postgres",
#                            password="1",
#                            host="localhost",
#                            port=5432)
#
#     cur = con.cursor()
#
#     def search_user(self , firstname):
#         query = """
#             select * from students where first_name = %s
#         """
#         params = (firstname,)
#         self.cur.execute(query , params)
#         students = self.cur.fetchall()
#         return students
#
#
# class Course:
#     def __init__(self , id , course_name , instructor):
#         self.id = id
#         self.course_name = course_name
#         self.instructor = instructor
#
#
#
#     def __repr__(self):
#         return f"{self.__dict__}"
#
# first_name = input("Search student : ")
# print(DB().search_user(first_name))
#
#
#
