import tkinter as tk
import Mode
import Constraints_GUI
import Modes_GUI

first = True

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

def switching(components, modes, numberComponents, numberModes):
    switchGUI = tk.Tk()

    def back():
        switchGUI.destroy()
        {mode.assignRequirement(varSwitch[modeName].get(), varRanking[modeName].get()) for modeName, mode in modes.items()}
        Modes_GUI.mode(components, modes, numberComponents, numberModes)
        global first
        first = False
    
    # Making the title, column headings, and ADD and CONTINUE which will 
    # always be in the GUI
    switchTitle = tk.Label(switchGUI, text = "MODES REQUIREMENTS")
    switchMods = tk.Label(switchGUI, text = "Mode")

    switchOptions = tk.Label(switchGUI, 
                            text = "When/Why Does Mission Enters Mode")

    switchRank = tk.Label(switchGUI, text = "Mode Rank")
    switchGap = tk.Label(switchGUI, text = "\t")

    switchContinue = tk.Button(switchGUI, 
                            text = "CONTIUE", 
                            command = switchGUI.destroy)

    switchBack = tk.Button(switchGUI, 
                        text = "BACK", 
                        command = back)
    
    # The title and headings will always be in the same place sin the 
    # GUI so I put them here to make later less cluttered
    switchTitle.grid(row = 0, column = 0, columnspan = 5)
    switchMods.grid(row = 1, column = 0)
    switchOptions.grid(row = 1, column = 1, columnspan = 4)
    switchRank.grid(row = 1, column = 5)
    switchGap.grid(row = 3 + numberComponents, column = 0)
    switchContinue.grid(row = 4 + numberModes, 
                        column = 0, 
                        columnspan = 6, 
                        sticky = tk.W + tk.E)
    #switchBack.grid(row = 5 + numberModes, 
    #               column = 0, 
    #               columnspan = 6, 
    #               sticky = tk.W + tk.E)
    # TODO: back button should be working but double check it

    varSwitch = {}
    switchModes = {}
    varRanking = {}
    modeRanking = {}
    OPTIONS = {
        "Random Interval": "Random",
        "Regular Interval": "Regular",
        "Power Constraint": "Power",
        "No Other Mode": "Background"
        }

    for (modeName, mode), switchModesRows in zip(modes.items(), range(numberModes)):
        varSwitch[modeName] = (tk.StringVar())
        # initialize
        varSwitch[modeName].set(mode.printRequirement()) 
        # Doesn't need to be list because it doesn't have a variable and
        # gets placed a few lines below
        switchMode = tk.Label(switchGUI, text = modeName) 
        varRanking[modeName] = (tk.IntVar())
        varRanking[modeName].set(mode.printRank())

        modeRanking[modeName] = tk.Entry(switchGUI, 
                                        textvariable = varRanking[modeName])
    
        for text, i in zip(OPTIONS, range(len(OPTIONS))):
            switchButtons = tk.Radiobutton(switchGUI, 
                                        text=text, 
                                        variable=varSwitch[modeName], 
                                        value=OPTIONS[text])

            switchButtons.grid(row = 2+switchModesRows, column = i+1)


        switchMode.grid(row = (2 + switchModesRows), column = 0)
        modeRanking[modeName].grid(row = (2+switchModesRows), 
                                column = len(OPTIONS)+1)
    
    switchGUI.mainloop()

    global first
    if (first):
        {mode.assignRequirement(varSwitch[modeName].get(), varRanking[modeName].get()) for modeName, mode in modes.items()}
        
        return Constraints_GUI.constraint(components, 
                                        modes, 
                                        numberComponents, 
                                        numberModes)

    else: 
        return components, modes, numberComponents, numberModes