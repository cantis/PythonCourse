import random
import tkinter

mainWindow = tkinter.Tk()

# setup the screen and frames for dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)

card_fram = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
