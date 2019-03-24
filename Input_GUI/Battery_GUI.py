import tkinter as tk

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

def runGUI():
    sim_GUI = tk.Tk()
    
    simTitle = tk.Label(sim_GUI, text = "Final Info")
    simFileLabel = tk.Label(sim_GUI, text = "STK Solar Panel Data")
    batteryLabel = tk.Label(sim_GUI, text = "Battery Energy (WHr)")
    startLabel = tk.Label(sim_GUI, text = "Battery Start Level")
    startUnitsLabel = tk.Label(sim_GUI, text = "Battery Start Units")
    timeStepLabel = tk.Label(sim_GUI, text = "STK Time Step (sec)")

    runSIM = tk.Button(sim_GUI, 
                    text = "CONTINUE", 
                    command = sim_GUI.destroy)
    
    simFileVariable = tk.StringVar()
    simFileVariable.set("C:\\Users\...\\MasterMonth_Program2.txt") 
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
    batteryLabel.grid(row = 2, column = 0, sticky = tk.E)
    batteryEntry.grid(row = 2, column = 1, columnspan = 2)
    startLabel.grid(row = 3, column = 0, sticky = tk.E)
    startEntry.grid(row = 3, column = 1, columnspan = 2)
    startUnitsLabel.grid(row = 4, column = 0, sticky = tk.E)
    unitWHR.grid(row = 4, column = 1)
    unitDOD.grid(row = 4, column = 2)
    timeStepLabel.grid(row = 5, column = 0, sticky = tk.E)
    timeStepEntry.grid(row = 5, column = 1, columnspan = 2)
    runSIM.grid(row = 6, column = 0, columnspan = 3, sticky = tk.W + tk.E)
    
    sim_GUI.mainloop()

    return batteryVariable.get(), startVariable.get(), startWHRVariable.get(), timeStepVariable.get()

