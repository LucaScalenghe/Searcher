# good reference for file usage
# https://www.geeksforgeeks.org/reading-writing-text-files-python/

import webbrowser as web
import os 
from pathlib import Path
from tkinter.messagebox import showinfo

def getPath():
    homeFolder = Path(os.getcwd())
    searcherFolder = Path('Searcher')   #name of the project folder
    subFolder = Path('domains.txt')     #name of the file where the project holds the domains
    path = homeFolder/searcherFolder
    path = path/subFolder
    return path


def search(text):
    file = open(getPath(), "r")
    domains = file.readlines()
    for DomainName in domains:
        web.open(DomainName + text)
    file.close()


def add_PageDomain(string):
    file = open(getPath(), "a")
    file.write("\n")
    file.write(string)
    file.close()

    # had to put the creation of a popUp messasge but couldn't put in the VisualInterface.py due to CIRCULAR IMPORT
    showinfo("Window", "Added")


def delete_domain():
    # todo
    # newWindow = tk.Toplevel(root)
    # newWindow.geometry("50x50")
    # text = tk.Label(root,"Added")
    # text.pack()
    pass


def showDomain():
    file = open(getPath(), "r")
    domains = file.readlines()
    file.close()
    return domains
