from project.Libruary.library_parts.auth.main import User
from project.Libruary.library_parts.book_crud.main import Book

session_user: User | None = None
categorys = ["Ilmiy", "Badiiy", "Fantastik"]


class UI:
    def main(self):
        global session_user
        menu = """
        1) register
        2) login
        3) exit
        >>>"""
        key = input(menu)
        try:
            match key:
                case "1":

                    user = {"first_name": input("First Name : "),
                            "phone_number": input("Phone number : ")}
                    obj = User(**user)
                    obj.isvalid()
                    card_id = obj.save()
                    print(f"Your card id : {card_id}")
                    print("Success create account !")
                    self.main()
                case "2":
                    card_id = input("Card id : ")
                    user = User(card_id=card_id)
                    session_user = user.select()
                    if session_user.card_id == "0580201649":
                        self.admin()
                    # self.account() # TODO
                    print(f"Welcome , {user.first_name}")

                case "3":
                    return
        except Exception as e:
            print(e)
            self.main()

    def admin(self):
        global session_user
        menu = """
        1) Books CRUD
        2) Users CRUD
        3) Settings
        4) logout 
        >>>"""
        key = input(menu)
        match key:
            case "1":
                self.book_crud()
            case "2":
                pass
                # self.user_crud() # TODO
            case "3":
                pass
                # self.settins_user() # TODO
            case "4":
                session_user = None
                self.main()

    def book_crud(self):
        global category
        menu = """
            1) add
            2) delete
            3) update
            4) book list
            0) <-back
            >>>"""
        key = input(menu)
        for i, category in enumerate(categorys, 1):
            print(f"{i}) {category}")
        print("0) <-back")
        if key != "0":
            category_key = int(input(">>>")) - 1
            category = categorys[category_key]
        try:
            match key:
                case "1":

                    book = {"category": category,
                            "name": input("Book name: "),
                            "author": input("Author :"),
                            "amount": input("Amount :")}
                    book = Book(**book)
                    book.isvalid()
                    book.save()
                    print("Success add !")
                    self.book_crud()
                case "2":
                    book_list: list[Book] = Book().book_list()
                    print(book_list)
                    for i, book in enumerate(book_list, 1):
                        print(f"{i}) {book.name} {book.author}")
                    print("0) <-back")
                    book_key = int(input(">>>")) - 1
                    book_list[book_key].delete()
                    print("Success delete !")
                    self.book_crud()
                case "3":
                    pass  # TODO
                case "4":
                    pass  # TODO
                case "0":
                    self.admin()  # TODO


        except Exception as e:
            print(e)
            self.book_crud()


UI().main()
