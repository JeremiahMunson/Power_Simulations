import tkinter as tk
import os
import sys

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

def runGUI():
    location = "C:\\Users\...\\MasterMonth_Program2.txt"

    first = True

    def cancel():
        print("Program Terminated")
        sys.exit()

    while(True):
        sim_GUI = tk.Tk()
    
        simTitle = tk.Label(sim_GUI, text = "Final Info")
        simFileLabel = tk.Label(sim_GUI, text = "STK Solar Panel Data")
        batteryLabel = tk.Label(sim_GUI, text = "Battery Energy (WHr)")
        startLabel = tk.Label(sim_GUI, text = "Battery Start Level")
        startUnitsLabel = tk.Label(sim_GUI, text = "Battery Start Units")
        timeStepLabel = tk.Label(sim_GUI, text = "STK Time Step (sec)")

        runSIM = tk.Button(sim_GUI, 
                        text = "RUN SIMULATION", 
                        command = sim_GUI.destroy)

        cancelProgram = tk.Button(sim_GUI, text = "CANCEL",
                            command = cancel)
    
        simFileVariable = tk.StringVar()
        simFileVariable.set(location) 
        errorTxt = "Could not find file at " + location
        simFileError = tk.Label(sim_GUI, text = errorTxt)
        simFileEntry = tk.Entry(sim_GUI, textvariable = simFileVariable)
        batteryVariable = tk.IntVar()
        batteryVariable.set(30)
        batteryEntry = tk.Entry(sim_GUI, textvariable = batteryVariable)
        startVariable = tk.IntVar()
        startVariable.set(28)
        startEntry = tk.Entry(sim_GUI, textvariable = startVariable)
        startWHRVariable = tk.BooleanVar()
        startWHRVariable.set(True)

        unitWHR = tk.Radiobutton(sim_GUI, 
                                text = "WHr", 
                                variable = startWHRVariable, 
                                value = True)

        unitDOD = tk.Radiobutton(sim_GUI, 
                                text = "DOD", 
                                variable = startWHRVariable, 
                                value = False)

        timeStepVariable = tk.IntVar()
        timeStepVariable.set(5)
        timeStepEntry = tk.Entry(sim_GUI, textvariable = timeStepVariable)
    
        simTitle.grid(row = 0, column = 0, columnspan = 3, sticky = tk.W + tk.E)
        simFileLabel.grid(row = 1, column = 0, sticky = tk.E)
        simFileEntry.grid(row = 1, column = 1, columnspan = 2)

        if(not first):
            simFileError.grid(row = 2, column = 0, 
                            columnspan = 3)

        batteryLabel.grid(row = 3, column = 0, sticky = tk.E)
        batteryEntry.grid(row = 3, column = 1, columnspan = 2)
        startLabel.grid(row = 4, column = 0, sticky = tk.E)
        startEntry.grid(row = 4, column = 1, columnspan = 2)
        startUnitsLabel.grid(row = 5, column = 0, sticky = tk.E)
        unitWHR.grid(row = 5, column = 1)
        unitDOD.grid(row = 5, column = 2)
        timeStepLabel.grid(row = 6, column = 0, sticky = tk.E)
        timeStepEntry.grid(row = 6, column = 1, columnspan = 2)
        runSIM.grid(row = 7, column = 0, columnspan = 3, sticky = tk.W + tk.E)
        cancelProgram.grid(row = 8, column = 0, columnspan = 3, sticky = tk.W + tk.E)

        sim_GUI.mainloop()

        location = simFileVariable.get()

        if(os.path.exists(location)):
            break
        else:
            first = False

    return batteryVariable.get(), startVariable.get(), startWHRVariable.get(), timeStepVariable.get()

