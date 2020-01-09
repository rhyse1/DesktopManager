from tkinter import *
from tkinter import messagebox

import CleanDesktop

Height = 1
Width = 20

def main():
    window = Tk()

    window.title("Desktop Cleaner - Main Menu")
    window.geometry("250x90")
    window.resizable(0,0)
    window.eval('tk::PlaceWindow %s center' % window.winfo_pathname(window.winfo_id()))

    menuLbl = Label(window, text = "Desktop Cleaner", font = ('Century Gothic',22))
    menuLbl.grid(columnspan = 4)

    cleanBttn = Button(text = "Clean Desktop", fg= "Black", command = lambda:cleanBttn_OnClicked(), font = ('Century Gothic',18), height = Height, width = Width)
    cleanBttn.grid(columnspan = 4)

    copyLbl = Label(window, text = "Rhys Evans, 2019", font = ('Century Gothic',10))
    copyLbl.grid(columnspan = 4)

    window.mainloop()


def cleanBttn_OnClicked():
    CleanDesktop.Clean()



if __name__ == '__main__':
	main()
