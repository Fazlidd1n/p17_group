products = ["Iphone14" , "Iphone13" , "Iphone12"]


def update(index , new_name):
    products[index] = new_name
    print(f"Successfully update !")

def show():
    for index , product in enumerate(products):
        print(f"{index}) {product}")



def delete(index: int):
    products.pop(index)


def add(product_name):
    products.append(product_name)


def main():
    while True:
        menu = """
            1) add product
            2) delete product
            3) update product
            4) show product
            5) search product 
            6) clear
            0) exit
            >>>""" # TODO : search , clear

        key: str = input(menu)

        if not (key.isdigit() and 1 <= int(key) <= 5):
            print("Key invalid !")
            continue

        if key == "1":
            product_name = input("Product name: ")
            add(product_name)
        elif key == "2":
            show()
            index = int(input("Index: "))
            delete(index)
        elif key == "3":
            show()
            index = int(input("Index: "))
            new_val = input("New name: ")
            update(index , new_val)
        elif key == "4":
            show()
        else:
            break

main()



