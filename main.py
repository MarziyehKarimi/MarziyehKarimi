from tkinter import Tk, ttk
from lib.guis import FileSearch,File,Filedelete

root = Tk()
root.title("مديريت فابل")


notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

File(notebook)

FileSearch(notebook)
Filedelete(notebook)

root.mainloop()
