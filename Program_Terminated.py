import tkinter as tk
import sys

def terminate():
    terminateGUI = tk.Tk()

    message = tk.Label(terminateGUI, text = "Program Terminated")
    

    message.grid(row = 1, column = 0)

    terminateGUI.mainloop()

