import datetime


class File:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return f.read()

    def write(self, data: str):
        with open(self.filename, "a") as f:
            f.write(data)

    def update(self, data: str):
        with open(self.filename, "w") as f:
            f.write(data)

    def clear(self):
        self.update("")





class Book:
    def __init__(self,
                 id=None,
                 category = None,
                 name=None,
                 author=None,
                 amount=None,
                 joint_at=datetime.datetime.now()):
        self.id = id
        self.category = category
        self.name = name
        self.author = author
        self.amount = amount
        self.join_at = str(joint_at)
        self.f = File("../UI/books.txt")

    def save(self):

        if not self.f.read():
            self.id = "1"
        else:
            self.id= str(int(self.f.read().split("\n")[-2].split('|')[0]) + 1)
        self.f.write("|".join(list(self.__dict__.values())[:-1]) + "\n")

    def edit(self , field, new_val):
        books = self.f.read().split("\n")
        for i, book in enumerate(books):
            if book.split("|")[0] == self.id:
                s = book.split("|")
                if field == "name":
                    s[1] = new_val
                elif field == "author":
                    s[2] = new_val
                books[i] = '|'.join(s)
                self.f.update('')
                for book in books:
                    self.f.write(book + "\n")

    def delete(self):
        books = self.f.read().split("\n")[:-1]
        for i, book in enumerate(books):
            if book.split('|')[0] == self.id:
                del books[i]
                self.f.update('')
                for book in books:
                    self.f.write(book + "\n")

    def isvalid(self):
        if not self.name.isalpha():
            raise Exception("Name must be alpha !")
        if not self.author.isalpha():
            raise Exception("Author must be alpha !")
        if not self.amount.isdigit():
            raise Exception("Amount must be number !")

    def book_list(self):
        books = []
        for i in self.f.read().split('\n')[:-1]:
            books.append(Book(*i.split("|")))
        return books

    def __repr__(self):
        return self.name


book1 = Book("1", "Xamsa", "Alisher", "-1")
book2 = Book("2", "Oqkema", "Chingiz", "10")
book3 = Book("3", "nmadir", "kimdir", "5")
book4 = Book("4", "nima", "kim", "530")


# try:
#     book2.isvalid()
#     book2.save()
# except Exception as e:
#     print(e)

# book2.edit("author", "Botirjon")

book1.delete()



