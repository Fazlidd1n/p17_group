# import tkinter as tk
from tkinter import *

users = []


def add():
    user = {
        "fullname": fullname.get(),
        "username": username.get(),
        "password": password.get()
    }
    fullname.set("")
    username.set("")
    password.set("")
    users.append(user)
    Label(register_win, text="Succesfuly register !").pack()


def account():
    screen.destroy()
    account_win = Tk()
    account_win.geometry("500x500")
    account_win.title("Account")
    Label(account_win, text="Welcome", font=(None, 30))

def check_login():
    for user in users:
        if user.get("username") == login_username.get() and user.get("password") == login_password.get():
            account()
    Label(login_win,text="Not found account !").pack()

def register():
    global fullname, username, password, register_win
    register_win = Toplevel(screen)
    register_win.title("Register")
    register_win.geometry("500x500")
    fullname = StringVar()
    username = StringVar()
    password = StringVar()
    Label(register_win, text="fullname : ", font=(None, 15)).pack(pady=10)
    Entry(register_win, textvariable=fullname, width=20).pack()
    Label(register_win, text="username : ", font=(None, 15)).pack(pady=10)
    Entry(register_win, textvariable=username, width=20).pack()
    Label(register_win, text="password : ", font=(None, 15)).pack(pady=10)
    Entry(register_win, textvariable=password, width=20).pack()
    Button(register_win, text="Submit", width=10, height=2, command=add()).pack(pady=10)

def login():
    global login_username, login_password
    login_win = Toplevel(screen)
    login_win.title("Register")
    login_win.geometry("500x500")
    login_username = StringVar()
    login_password = StringVar()

    Label(login_win, text="username : ", font=(None, 15)).pack(pady=10)
    Entry(login_win, textvariable=login_username, width=20).pack()
    Label(login_win, text="password : ", font=(None, 15)).pack(pady=10)
    Entry(login_win, textvariable=login_password, width=20).pack()
    Button(login_win, text="Submit", width=10, height=2, command=check_login).pack(pady=10)

def show_user():
    show_win = Toplevel(screen)
    for i in users:
        Label(show_win, text=f"{i}")

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("450x300")
    screen.title("Login or Register")
    Button(screen, text="Register", width=10, height=2, command=register).pack(pady=20)
    Button(screen, text="Login", width=10, height=2, command=login).pack(pady=20)

    screen.mainloop()

main_screen()
