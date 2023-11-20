"""CSV FILE CLASS"""
# import pandas as pd
#
# class File:
#     def __init__(self, filename):
#         self.filename = filename
#     def read(self):
#         df = pd.read_csv(self.filename)
#         return df
#     def write(self, data: dict):
#         df = pd.DataFrame(data)
#         df.to_csv(self.filename, index=False, sep='\t')
#
#
#
# data = {
#     'Name': ['John', 'Alice', 'Bob'],
#     'Age': [28, 24, 22],
#     'City': ['New York', 'San Francisco', 'Los Angeles']
# }
#
# File("data.csv").write(data)
# print(File("data.csv").read())

"""JSON FILE CLASS"""
# import pandas as pd
#
#
# class File:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def read(self):
#         df = pd.read_json("data.json")
#         return df
#
#     def write(self, data: dict):
#         df = pd.DataFrame(data)
#         df.to_json(self.filename, index=False)
#
#
# data = {
#     "Duration": {
#         "0": 60,
#         "1": 60,
#         "2": 60,
#         "3": 45,
#         "4": 45,
#         "5": 60
#     },
#     "Pulse": {
#         "0": 110,
#         "1": 117,
#         "2": 103,
#         "3": 109,
#         "4": 117,
#         "5": 102
#     },
#     "Maxpulse": {
#         "0": 130,
#         "1": 145,
#         "2": 135,
#         "3": 175,
#         "4": 148,
#         "5": 127
#     },
#     "Calories": {
#         "0": 409,
#         "1": 479,
#         "2": 340,
#         "3": 282,
#         "4": 406,
#         "5": 300
#     }
# }
#
# print(File("data.json").read())

"""PDF dan RASMLARNI AJRATIB OLISH"""
# import fitz
#
# def extract_images_from_pdf(pdf_file):
#     try:
#         pdf_document = fitz.open(pdf_file)
#         for page_num in range(len(pdf_document)):
#             page = pdf_document.load_page(page_num)
#             image_list = page.get_images(full=True)
#
#             for img_index, img in enumerate(image_list):
#                 xref = img[0]
#                 base_image = pdf_document.extract_image(xref)
#                 image_data = base_image["image"]
#
#                 image_format = base_image["ext"]
#
#                 with open(f"image_{page_num + 1}_{img_index + 1}.{image_format}", "wb") as image_file:
#                     image_file.write(image_data)
#
#         print(f"Rasmlar ushbu '{pdf_file}' joyga saqlandi.")
#
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#
# pdf_file_path = "/Users/macbookpro/PycharmProjects/p17_group/Module_3/Lesson_8/my.pdf"
# extract_images_from_pdf(pdf_file_path)


"""EXCEL"""
#
# import pandas as pd
# from sqlalchemy import create_engine
#
# def excel_to_sqlite(excel_file, sqlite_file, table_name):
#     df = pd.read_excel(excel_file, engine='openpyxl')
#
#     engine = create_engine(f'sqlite:///{sqlite_file}')
#
#     df.to_sql(table_name, engine, if_exists='replace', index=True)
# if __name__ == "__main__":
#     excel_file_path = "/Users/macbookpro/PycharmProjects/p17_group/Module_3/Lesson_8/eng-uzbek.xlsx"
#     sqlite_file_path = "/Users/macbookpro/PycharmProjects/p17_group/Module_3/Lesson_8/vocabulary.sqlite"
#     table_name = "vocabulary"
#
#     excel_to_sqlite(excel_file_path, sqlite_file_path, table_name)
