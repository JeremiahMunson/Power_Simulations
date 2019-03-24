import tkinter as tk
import Mode
import Lighting_GUI
import ModeSwitching_GUI

first = True

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

def constraint(components, modes, numberComponents, numberModes):
    constraintGUI = tk.Tk()

    def back():
        constraintGUI.destroy()
        {mode.inputRequirementConstraints(varFirstEntry[modeName].get(), varFirstOption[modeName].get(), varSecondEntry[modeName].get(), varSecondOption[modeName].get()) for modeName, mode in modes.items()}
        
        ModeSwitching_GUI.switching(components, 
                                    modes, 
                                    numberComponents, 
                                    numberModes)
        global first 
        first = False

    constraintTitle = tk.Label(constraintGUI, 
                            text = "Mode Requirement Constraints")

    frequencyLowPwr = tk.Label(constraintGUI, 
                            text = "Frequency/Low Power")

    durationHighPwr = tk.Label(constraintGUI, 
                            text = "Duration/Recover Power")

    constraintGap = tk.Label(constraintGUI, 
                            text = "\t")

    constraintContinue = tk.Button(constraintGUI, 
                            text = "CONTINUE", 
                            command = constraintGUI.destroy)

    constraintBack = tk.Button(constraintGUI, 
                            text = "BACK", 
                            command = back)

    constraintTitle.grid(row = 0, column = 0, columnspan = 7)
    frequencyLowPwr.grid(row = 1, column = 1, columnspan = 3)
    durationHighPwr.grid(row = 1, column = 4, columnspan = 3)
    constraintGap.grid(row = 3 + numberModes, column = 0)

    constraintContinue.grid(row = 4 + numberModes, 
                            column = 0, 
                            columnspan = 7, 
                            sticky = tk.W + tk.E)

    constraintBack.grid(row = 5 + numberModes, 
                        column = 0, 
                        columnspan = 7, 
                        sticky = tk.W + tk.E)

    varFirstEntry = {}
    firstEntryBox = {}
    varSecondEntry = {}
    secondEntryBox = {}
    varFirstOption = {}
    varSecondOption = {}

    FREQUENCY = {
        "/orbit":"/orbit",
        "/day":"/day"
        }
    
    DODWHR = {
        "DoD":"DoD",
        "WHr":"WHr"
        }

    DURATION = {
        "sec":"sec",
        "min":"min"
        }

    for (modeName, mode), k in zip(modes.items(), range(numberModes)):
        req, beginMode, beginUnits, endMode, endUnits = mode.printReqConstraints()
        varFirstEntry[modeName] = (tk.StringVar())
        varFirstEntry[modeName].set(beginMode)
        varSecondEntry[modeName] = (tk.StringVar())
        varSecondEntry[modeName].set(endMode)
        varFirstOption[modeName] = (tk.StringVar())
        varFirstOption[modeName].set(beginUnits)
        varSecondOption[modeName] = (tk.StringVar())
        varSecondOption[modeName].set(endUnits)

        if(mode.printRequirement() != "Background"):
            constraintModes = tk.Label(constraintGUI, text = modeName)
            constraintModes.grid(row = 2 + k, column = 0)
  
            firstEntryBox[modeName] = tk.Entry(constraintGUI, 
                                    textvariable = varFirstEntry[modeName])
            firstEntryBox[modeName].grid(row = 2 + k, column = 1)

            secondEntryBox[modeName] = tk.Entry(constraintGUI, 
                                    textvariable = varSecondEntry[modeName])
            secondEntryBox[modeName].grid(row = 2 + k, column = 4)

            #varFirstOption[modeName].set("NA")
            #varSecondOption[modeName].set("NA")
###############################################################################
            for textFreq, textDur, textDOD, optionsCol in zip(FREQUENCY, DURATION, DODWHR, range(len(FREQUENCY))):
                if(mode.printRequirement() == "Regular" 
                        or mode.printRequirement() == "Random"):
                    firstOptions = tk.Radiobutton(constraintGUI, 
                                                text = textFreq,
                                                variable = varFirstOption[modeName], 
                                                value = FREQUENCY[textFreq])

                    firstOptions.grid(row = 2+k, 
                                    column = optionsCol+2, 
                                    sticky = tk.W)

                    secondOptions = tk.Radiobutton(constraintGUI, 
                                                text = textDur, 
                                                variable = varSecondOption[modeName], 
                                                value = DURATION[textDur])

                    secondOptions.grid(row = 2+k, 
                                    column = optionsCol+5, 
                                    sticky = tk.W)
                elif(mode.printRequirement() == "Power"):
                    firstOptions = tk.Radiobutton(constraintGUI, 
                                                text = textDOD, 
                                                variable = varFirstOption[modeName], 
                                                value = DODWHR[textDOD])
                    
                    firstOptions.grid(row = 2+k, 
                                    column = optionsCol+2, 
                                    sticky = tk.W)
                    
                    secondOptions = tk.Radiobutton(constraintGUI, 
                                                text = textDOD, 
                                                variable = varSecondOption[modeName], 
                                                value = DODWHR[textDOD])
                    
                    secondOptions.grid(row = 2+k, 
                                    column = optionsCol+5, 
                                    sticky = tk.W)

        else:
            na = tk.StringVar()
            na.set("NA")
            varFirstEntry[modeName] = na
            varFirstOption[modeName] = na
            varSecondEntry[modeName] = na
            varSecondOption[modeName] = na
    
    constraintGUI.mainloop()

    global first

    if(first):
        {mode.inputRequirementConstraints(varFirstEntry[modeName].get(), varFirstOption[modeName].get(), varSecondEntry[modeName].get(), varSecondOption[modeName].get()) for modeName, mode in modes.items()}
        return Lighting_GUI.lighting(components, modes, numberComponents, numberModes)
    else: 
        return components, modes, numberComponents, numberModes