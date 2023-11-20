# N1 --> karzinka
# products = ["Iphone 14", "Iphone 13", "Iphone 12"]
#
#
# def add(product: str):
#     products.append(product)
#     print(f"Successfully add !")
#
#
# def delete(index: int):
#     products.pop(index)
#     print(f"Successfully delete !")
#
#
# def update(index: int , new_name: str):
#     products[index] = new_name
#     print(f"Successfully update !")
#
#
# def show():
#     for i, v in enumerate(products):
#         print(f"{i}) {v}")
#
#
# def search(product_name):
#     for i , v in enumerate(products):
#         if v.startswith(product_name) | v.endswith(product_name):
#             print(f"{i}) {v}")
#
#
# def clear():
#     products.clear()
#     print(f"Successfully clear !")
#
#
# def main():
#     while True:
#         menyu: str = """
#         1) add product
#         2) delete product
#         3) update product
#         4) show product
#         5) search product
#         6) clear
#         0) exit
#         >>>"""
#         key: str = input(menyu)
#         if key == "1":
#             product: str = input("product name : ")
#             add(product)
#         if key == "2":
#             show()
#             index = int(input("product index : "))
#             delete(index)
#         if key == "3":
#             show()
#             index = int(input("product index : "))
#             new_name = input("new name : ")
#             update(index, new_name)
#         if key == "4":
#             show()
#         if key == "5":
#             product_name = input("product name : ")
#             search(product_name)
#         if key == "6":
#             clear()
#         if key == "0":
#             break
#
#
# main()

#N2
# s = input("s = ")
# k: int = int(input("k = "))
# result: list = s.split()
# for i, v in enumerate(result):
#     if i < k:
#         print(v,end=" ")

#N3
# len_list: int = int(input("List uzunligi : "))
# nums: list = []
# i = 0
# while i < len_list:
#     element: int = int(input(f"{i+1}-element -> "))
#     nums.append(element)
#     i += 1
#
# nums.extend(nums)
# print(nums)

#N4
# import random
# nums: list = [0, 2, 1, 5, 3, 4]
# random.shuffle(nums)
# print(nums)

#N5
# words: list = ["hey","aeo","mu","ooo","artro"]
# arr: list = []
# for word in words:
#     count: int = 0
#     for i in word:
#         if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
#             count += 1
#     arr.append(count)
#
# print(arr)

#N6
# def count_sentences(text):
#     sentence_end_chars = {'.', '?', '!', '...'}
#     count = 0
#     index = 0
#     while index < len(text):
#         if text[index] in sentence_end_chars:
#             count += 1
#         index += 1
#
#     return count
#
#
# text: str = input("Enter text: ")
# num_sentences = count_sentences(text)
# print(f"Number of sentences: {num_sentences}")