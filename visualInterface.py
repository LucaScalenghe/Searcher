import tkinter as tk
from pageManager import search, add_PageDomain, showDomain


def new_TextLabel(root, string):
    return tk.Label(root, text=string)


def new_Root():
    root = tk.Tk()
    root.geometry("500x30")
    root.title("Searcher")
    return root


def new_SearchBox(root):
    search_box = tk.Entry(root, width=50)
    search_box.bind("<Return>", (lambda event: search(search_box.get())))
    return search_box


def new_AddBox(root):
    add_box = tk.Entry(root, width=50)
    add_box.bind("<Return>", (lambda event: add_PageDomain(add_box.get())))
    return add_box


def secondPageWindow(root, dim):
    # shows all the pages you added
    newWindow = tk.Toplevel(root)
    newWindow.geometry(dim)
    text = new_TextLabel(newWindow, showDomain())
    add_box = new_AddBox(newWindow)

    # organizing my elements on the window
    text.grid(row=0, column=0)
    add_box.grid(row=1, column=0)


def new_Window():
    root = new_Root()
    text = new_TextLabel(root, "Search")
    search_box = new_SearchBox(root)
    button = tk.Button(root,
                       text="Add Page",
                       command=lambda: secondPageWindow(root, "500x100"))

    # organizing my elements on the window
    text.grid(row=0, column=0)
    search_box.grid(row=0, column=1)
    button.grid(row=0, column=2)

    root.mainloop()

