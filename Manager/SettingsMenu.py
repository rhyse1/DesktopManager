from tkinter import *
from tkinter import messagebox

import CleanDesktop
import SettingsMenu

Height = 1
Width = 20

def main():
    # Creating the window object
    window = Tk()

    # Defining window properties
    window.title("Main Menu")
    window.geometry("310x170")
    window.resizable(0,0) # Makes the window locked to the definend resolution

    # Creating the label that displays the current menu header
    menuLbl = Label(window, text = "Desktop Cleaner", font = ('Century Gothic',22))
    menuLbl.grid(columnspan = 4) # Defining the widget's constraints

    # Creating the report - stock button
    cleanBttn = Button(text = "Clean Desktop", fg= "Black", command = lambda:cleanBttn_OnClicked(window), font = ('Century Gothic',18), height = Height, width = Width)
    cleanBttn.grid(columnspan = 4) # Defining the widget's constraints

    otherBttn = Button(text = "Settings", fg= "Black", command = lambda:cleanBttn_OnClicked(window), font = ('Century Gothic',18), height = Height, width = Width)
    otherBttn.grid(columnspan = 4) # Defining the widget's constraints


    copyLbl = Label(window, text = "Rhys Evans, 2019", font = ('Century Gothic',10))
    copyLbl.grid(columnspan = 4) # Defining the widget's constraints

    window.mainloop()


def cleanBttn_OnClicked(window):
    window.destroy()
    


if __name__ == '__main__':
	main()
