import datetime
import random
from tkinter import *
from project.Bankomat_tkinter.auth.main import User
from project.Bankomat_tkinter.DB.main import File


def random_card_number():
    codes = ["9860", "8600", "6262", "5656", "6767", "5555"]
    return f"{random.choice(codes)}{str(random.randint(1, 10000)).zfill(4)}{str(random.randint(1, 10000)).zfill(4)}{str(random.randint(1, 10000)).zfill(4)}"


class UI:
    win = Tk()

    def balance(self):
        try:
            self.win.destroy()
            self.win = Tk()
            self.win.geometry("500x500")
            self.win.title("Balance")
            Button(self.win, text='🔙', bg='green', font=(None, 20, "bold"), command=self.main3).place(x=25, y=25)
            users = File("users.json").read()
            for user in users:
                if user.get("card_number") == str(self.card.get()) and user.get("password") == str(self.pasword.get()):
                    Label(self.win, text=f"Your balance : {user.get('balance')}", fg="white",
                          font=(None, 20, "bold")).place(x=150, y=200)
                    break
            else:
                raise Exception("Error ❗️")
        except Exception as e:
            Label(self.win, text=e, font=(None, 15, "bold"), fg="red").pack(extand=True)

    def transfer_submit(self):
        try:
            users = File("users.json").read()
            for i, user in enumerate(users):
                if users[self.id]["balance"] < int(self.transfer_sum.get()):
                    raise Exception("Balanceda pul yetarli emas ❗️")
                if user.get("card_number") == str(self.transfer_card.get()) and users[self.id][
                    "balance"] >= int(self.transfer_sum.get()):
                    users[self.id]["balance"] -= int(self.transfer_sum.get())
                    print(users[self.id]["balance"])
                    users[i]["balance"] += int(self.transfer_sum.get())
                    print(users[i]["balance"])
                    print("pul ketdi")
                    Label(self.win, text="Succesfully tranfer ✅", font=(None, 20, "bold")).place(x=150)
                    break
            else:
                raise Exception("Not found this card number ❗️")
            File("users.json").write(users)
        except Exception as e:
            Label(self.win, text=e, fg="red", font=(None, 15, "bold")).place(x=30)

    def transfer(self):
        self.win.destroy()
        self.win = Tk()
        self.win.geometry("500x500")
        self.win.title("Transfer money")
        self.transfer_card = StringVar()
        self.transfer_sum = StringVar()
        Button(self.win, text='🔙', bg='green', font=(None, 20, "bold"), command=self.main3).place(x=25, y=25)
        Label(self.win, text="card number", font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.transfer_card, font=(None, 20, "bold")).pack(expand=True)
        Label(self.win, text="summa", font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.transfer_sum, font=(None, 20, "bold")).pack(expand=True)
        Button(self.win, text="Submit", font=(None, 14, "bold"), command=self.transfer_submit).pack(expand=True)

    def show_card_numbber(self):
        self.win.destroy()
        self.win = Tk()
        self.win.geometry("500x500")
        Button(self.win, text='🔙', bg='green', font=(None, 20, "bold"), command=self.main2).place(x=25, y=25)
        Label(self.win, text=f"Your card number : {self.card_number}", font=(None, 20, "bold")).pack(expand=True)
        # Button(self.win, text="Okey✅", command=self.main).pack(expand=True)

    def register_submit(self):
        try:
            self.date = datetime.datetime.now()
            self.card_number = random_card_number()
            user = {
                "fullname": self.fullname.get(),
                "email": self.email.get(),
                "password": self.password.get(),
                "balance": 50000,
                "card_number": self.card_number,
            }
            user = User(**user)
            user.create_id()
            user.is_valid()
            user.save()
            self.show_card_numbber()
        except Exception as e:
            Label(self.win, text=e, fg="red").place(x=250, y=0)

    def register(self):
        self.win.destroy()
        self.win = Tk()
        self.fullname = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.win.geometry("600x600")
        self.win.title("Register")
        Button(self.win, text='🔙', bg='green', font=(None, 20, "bold"), command=self.main2).place(x=25, y=25)
        Label(self.win, text="Register", fg="blue", font=(None, 40, "bold")).pack()
        Label(self.win, text='Full Name', font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.fullname, font=(None, 20, "bold")).pack()
        Label(self.win, text='Email Name', font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.email, font=(None, 20, "bold")).pack()
        Label(self.win, text='Password', font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.password, font=(None, 20, "bold")).pack()
        Button(self.win, text="Submit", bg="green", font=(None, 14, "bold"), command=self.register_submit).pack(
            expand=True)

        self.win.mainloop()

    def login_submit(self):
        try:
            self.id = 0
            users = File("users.json").read()
            for i, user in enumerate(users):
                if user.get("card_number") == str(self.card.get()) and user.get("password") == str(self.pasword.get()):
                    self.id = i
                    users[i]["update_at"] = str(datetime.datetime.now())
                    self.main3()
                    break
            else:
                raise Exception("Not found account ❌")
            File("users.json").write(users)

        except Exception as e:
            Label(self.win, text=e, font=(None, 15, "bold"), fg="red").place(x=10)

    def login(self):
        self.win.destroy()
        self.win = Tk()
        self.card = StringVar()
        self.pasword = StringVar()
        self.win.geometry("400x400")
        self.win.title("Login")
        Button(self.win, text='🔙', bg='green', font=(None, 20, "bold"), command=self.main2).place(x=25, y=25)
        Label(self.win, text="card number", font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.card, font=(None, 20, "bold")).pack(expand=True)
        Label(self.win, text="password", font=(None, 20, "bold")).pack(expand=True)
        Entry(self.win, textvariable=self.pasword, font=(None, 20, "bold")).pack(expand=True)
        Button(self.win, text="Submit", font=(None, 14, "bold"), command=self.login_submit).pack(expand=True)
        self.win.mainloop()

    def main(self):
        self.win.geometry("500x400")
        self.win.title("Bankomat_tkinter")
        Label(self.win, text="Bankomat_tkinter", font=(None, 35, "bold")).pack(pady=50)
        Button(self.win, text='Register', bg='green', font=(None, 15, "bold"), width=7, command=self.register).place(
            x=190, y=130)
        Button(self.win, text='Login', bg='blue', font=(None, 15, "bold"), width=7, command=self.login).place(x=190,
                                                                                                              y=180)
        Button(self.win, text='Exit', bg='red', font=(None, 15, "bold"), width=7,
               command=lambda: self.win.destroy()).place(x=190, y=230)

        self.win.mainloop()

    def main2(self):
        self.win.destroy()
        self.win = Tk()
        self.win.geometry("500x400")
        self.win.title("Bankomat_tkinter")
        Label(self.win, text="Bankomat_tkinter", font=(None, 35, "bold")).pack(pady=50)
        Button(self.win, text='Register', bg='green', font=(None, 15, "bold"), width=7, command=self.register).place(
            x=190, y=130)
        Button(self.win, text='Login', bg='blue', font=(None, 15, "bold"), width=7, command=self.login).place(x=190,
                                                                                                              y=180)
        Button(self.win, text='Exit', bg='red', font=(None, 15, "bold"), width=7,
               command=lambda: self.win.destroy()).place(x=190, y=230)

        self.win.mainloop()

    def main3(self):
        self.win.destroy()
        self.win = Tk()
        self.win.geometry("500x400")
        self.win.title("Bankomat_tkinter")
        Button(self.win, text="Transfer money", font=(None, 15, "bold"), width=10, command=self.transfer).place(
            x=190, y=130)
        Button(self.win, text="Balance", font=(None, 15, "bold"), width=10, command=self.balance).place(x=190, y=180)
        Button(self.win, text="Log out", font=(None, 15, "bold"), width=10, command=self.main2).place(x=190, y=230)


if __name__ == '__main__':
    UI().main()
