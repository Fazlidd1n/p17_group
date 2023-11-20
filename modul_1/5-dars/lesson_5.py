# N1 ---> Karzinka :
def Karzinka(a: int):
    mahsulot: str
    if a == 1:
        mahsulot = input("Nma mahsulot qo'shasiz : ")
        products.append(mahsulot)
        print("Mahsulot qo'shildi !")
    elif a == 2:
        mahsulot = input("Qaysi mahsulotni olip tashlamoqchisiz : ")
        products.remove(mahsulot)
        print("Mahsulot olip tashlandi !")
    elif a == 3:
        print(products)
    elif a == 4:
        print("Mahsulot uzunligi :",len(products))
    else:
        print("Noto'g'ri tanlov !")
text: str = """
1 - " mahsulot qo'shish "
2 - " mahsulotni olip tashlash "
3 - " mahsulotlarni ko'rsatish "
4 - " cout product "
"""
products=[]
while True:
    print(text)
    Karzinka(int(input("Tanlovingiz : ")))
