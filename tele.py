import os
from tkinter import Tk, Label, Button, filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    path_label.config(text=filename)

def browseFolders():
    dirname = filedialog.askdirectory(initialdir = "/", title = "Select a Folder")
    path_label.config(text=dirname)

def createFile():
    filename = filedialog.asksaveasfilename(initialdir = "/", title = "Create a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    if filename:
        with open(filename, 'w') as f:
            f.write("This is a new file.")

root = Tk()
root.geometry("300x200")

bfile = Button(root, text="Browse Files", command=browseFiles)
bfile.pack()

bfolder = Button(root, text="Browse Folders", command=browseFolders)
bfolder.pack()

bcreate = Button(root, text="Create File", command=createFile)
bcreate.pack()

path_label = Label(root, text="")
path_label.pack()

root.mainloop()
