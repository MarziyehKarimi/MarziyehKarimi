from tkinter import Button, Entry, ttk, Label, Frame, StringVar, messagebox, Listbox, Toplevel
from lib.tree import insert, search,deleteNode

class File:
    def __init__(self, master):
        file = Frame(master, relief="groove", width=200, height=200)
        master.add(file, text="چهارراه")

        Label(file, text="اضافه کردن چهارراه").pack(
            padx=10, pady=10, side="top", anchor="nw")

        Label(file, text="نام فايل").pack(
            padx=10, pady=10, side="top", anchor="nw")
        file_name = Entry(file)
        file_name.pack(padx=10, pady=10, side="top", anchor="nw")

        Label(fourway, text="اذرس فايل").pack(
            padx=10, pady=10, side="top", anchor="nw")
        adres = Entry(file)
        adres.pack(padx=10, pady=10, side="top", anchor="nw")

        Label(fourway, text="سايز فايل").pack(
            padx=10, pady=10, side="top", anchor="nw")
        size = Entry(file)
        size.pack(padx=10, pady=10, side="top", anchor="nw")


        def save_fourway():
            file_name = file_name.get()
            dres= adres.get()
            size = size.get()

            with open("db/file.txt", "a", encoding="utf-8") as file:
                file.write(f"{name}-{adres_}-{size}")

            messagebox.showinfo("", "Done :)")

        Button(file, text="ذخیره اطلاعات",
               command=save_file).pack(padx=10, pady=10)
