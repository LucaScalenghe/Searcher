# https://stackoverrun.com/it/q/4624672
# taught me how to use bind function in order to use it for opening 
# my pages with the "enter click"

# from tkinter import *
# from tkinter.messagebox import showinfo

# def reply(name):
#        showinfo(title="Reply", message = "Hello %s!" % name)


# top = Tk()
# top.title("Echo")


# Label(top, text="Enter your name:").pack(side=TOP)
# ent = Entry(top)
# ent.bind("<Return>", (lambda event: reply(ent.get())))
# ent.pack(side=TOP)
# btn = Button(top,text="Submit", command=(lambda: reply(ent.get())))
# btn.pack(side=LEFT)

# top.mainloop()



# How to open a new window in tkinter
# https://www.delftstack.com/it/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/

# import tkinter as tk

# def createNewWindow():
#     newWindow = tk.Toplevel(app)
#     labelExample = tk.Label(newWindow, text = "New Window")
#     buttonExample = tk.Button(newWindow, text = "New Window button")

#     labelExample.pack()
#     buttonExample.pack()




# app = tk.Tk()
# buttonExample = tk.Button(app, 
#               text="Create new window",
#               command=createNewWindow)
# buttonExample.pack()

# app.mainloop()


#how to pass arguments in the command of a button 
# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter


# https://www.youtube.com/watch?v=dyUhGZ6iNTc
# import requests
# import sys
# import webbrowser
# import bs4

# nomePagina = 'ciao'
# res = requests.get('https://google.com/search?q=' + ''.join(nomePagina))

# res.raise_for_status()

# soup = bs4.BeautifulSoup(res.text, "html.parser")
# linkElements = soup.select('.r a')
# linkToOpen = min(5, len(linkElements))
# for i in range(linkToOpen):
#        webbrowser.open('https://google.com' + linkElements[i].get('href'))


#how to open youtube and google
# https://www.youtube.com/watch?v=pSYlr87QNEU
# import webbrowser

# name = 'something'
# webbrowser.open('https://google.com/?#q=' + name)
# webbrowser.open('https://www.youtube.com/results?search_query=' + name)
# webbrowser.open('https://www.amazon.it/s?k=' + name)
