import tkinter as tk
import Mode
import Components_GUI

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

def size(components, modes):
    sizeGUI = tk.Tk()

    sizeTitle = tk.Label(sizeGUI, text = "NUMBER OF COMPONENTS AND MODES")
    numComponentsLabel = tk.Label(sizeGUI, text = "Number of Components")
    numModesLabel = tk.Label(sizeGUI, text = "Number of Modes")
    sizeGap = tk.Label(sizeGUI, text = "\t")

    sizeContinue = tk.Button(sizeGUI, 
                            text = "CONTINUE", 
                            command = sizeGUI.destroy)

    numComponentsVariable = tk.StringVar()
    numComponentsVariable.set(3)
    numModesVariable = tk.StringVar()
    numModesVariable.set(4)

    numComponentsInput = tk.Entry(sizeGUI, 
                                textvariable = numComponentsVariable)

    numModesInput = tk.Entry(sizeGUI, textvariable = numModesVariable)

    sizeTitle.grid(row = 0, 
                column = 0, 
                columnspan = 2, 
                sticky = tk.W + tk.E)

    numComponentsLabel.grid(row = 1, column = 0)
    numModesLabel.grid(row = 2, column = 0)
    numComponentsInput.grid(row = 1, column = 1)
    numModesInput.grid(row = 2, column = 1)
    sizeGap.grid(row = 3, column = 0)

    sizeContinue.grid(row = 4, 
                    column = 0, 
                    columnspan = 2, 
                    sticky = tk.W + tk.E)

    sizeGUI.mainloop()

    return Components_GUI.comp(components, 
                            modes, 
                            int( numComponentsVariable.get()), 
                            int(numModesVariable.get()))