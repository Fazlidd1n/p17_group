# class :
#     ShoppingCart(items: dict)
#         def : add_item , remove_item , view_cart

class ShoppingCart:
    def __init__(self, items: dict):
        self._items: dict[items] = {}

    def add_item(self):
        item = {
            "name": input("Name: "),
            "price": int(input("Price: ")),
            "quantity": int(input("Quantity: "))
        }
        self._items.update(**item)

    def remove_item(self, name: str):
        self._items.pop(name)

    def view_cart(self):
        for _ in self._items:
            print(
                "Products:\n"
                f"Name: {self._items}"
            ) # TODO