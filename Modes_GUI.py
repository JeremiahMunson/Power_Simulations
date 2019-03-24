import tkinter as tk
import Mode
import ModeSwitching_GUI
import Components_GUI

first = True

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

def mode(components, modes, numberComponents, numberModes):
    modeGUI = tk.Tk()

    if(len(modes) > 0):
        fakeModes = {}
        for (modeName, mode), k in zip(modes.items(), range(len(modes))):
            fakeModes[k] = mode

    def back():
        modeGUI.destroy()
        nonlocal modes
        nonlocal components
        nonlocal numberComponents
        nonlocal numberModes
        # Dict of 1's and 0's where 1 is component is used and 
        # 0 is component not used
        compsInMode = {}
        for modeNumber in range(numberModes):
            compsInMode = {componentName: modeCompChecks[modeNumber][componentName].get() for componentName in components}
            modes[varModeNames[modeNumber].get()] = Mode.Mode(
                                                            varModeNames[modeNumber].get(), 
                                                            components, 
                                                            compsInMode)
        global first
        first = False
        components, modes, numberComponents, number = Components_GUI.comp(components, 
                                                                        modes, 
                                                                        numberComponents, 
                                                                        numberModes)
    
    # Making the title, column headings, and ADD and CONTINUE which will always be in the GUI
    modeTitle = tk.Label(modeGUI, text = "MODES")
    modeNameHead = tk.Label(modeGUI, text = "Name")
    modeCompHead = tk.Label(modeGUI, text = "Components Operating in Mode")
    modeGap = tk.Label(modeGUI, text = "\t")

    modeContinue = tk.Button(modeGUI, 
                            text = "CONTIUE", 
                            command = modeGUI.destroy)

    modeBack = tk.Button(modeGUI, text = "BACK", command = back)
    
    # The title and headings will always be in the same place sin the 
    # GUI so I put them here to make later less cluttered
    modeTitle.grid(row = 0, column = 0, columnspan = 3)
    modeNameHead.grid(row = 1, column = 1)
    modeCompHead.grid(row = 1, column = 2, columnspan = numberComponents)
    modeGap.grid(row = numberModes + 2, column = 0)

    modeContinue.grid(row = numberModes + 3, 
                    column = 0, 
                    columnspan = 2 + numberComponents, 
                    sticky = tk.W + tk.E)

    #modeBack.grid(row = numberModes + 4, column = 0, columnspan = 2 + numberComponents, sticky = tk.W + tk.E)
        
    
    # The mode name ENTRY BOX array. 
    # Same as 'compName' from components but for modes
    modeNameEntry = {}
    # Array of tkinter string variables of the mode name. 
    # Same as 'varCompNames' from components
    varModeNames = {} 
    # dict of tkinter checkboxes, one for each component in the satellite
    modeComps = {}
    # dict of tkinter integer variables for the checkboxes,
    # one for each component
    varModeCompChecks = {}
    # list of 'varModeCompChecks' used to keep track of which components 
    # are in use for each mode 
    modeCompChecks = {} 
    # List of modeComps (list of lists of checkboxes) where ... 
    # modeCompsRow[row/mode][component checkbox]
    modeCompsRow = {}
    for modeNumber in range(numberModes):
        # Makes the mode name input string and adds it to the list of 
        # mode names
        varModeNames[modeNumber] = tk.StringVar()
        if(len(modes) == 0):
            varModeNames[modeNumber].set("Mode" + str(modeNumber+1))
        else:
            varModeNames[modeNumber].set(fakeModes[modeNumber].name())
            

        
        # Makes a new "Mode " label and mode name input box and 
        # adds them to the lists
        modeNameLabel = tk.Label(modeGUI, 
                                text = "Mode " + str(modeNumber + 1))

        modeNameEntry[modeNumber] = tk.Entry(modeGUI, 
                                            textvariable = varModeNames[modeNumber])
        
        # Clears the arrays specific to each row to make sure they 
        # aren't running over one row to another
        varModeCompChecks = {}
        modeComps = {}
        
        # Makes input needed for checkboxes (different modes) and adds it 
        # to a list and adds the actual checkboxes to a list of checkboxes
        if(len(modes) > 0):
            for modeIndex in fakeModes:
                for componentName, compPower in components.items():
                    varModeCompCheck = tk.IntVar()
                    varModeCompCheck.set(0)
                    for compName in fakeModes[modeIndex].components():
                        if (compName == componentName):
                            varModeCompCheck.set(1)
                    varModeCompChecks[componentName] = (varModeCompCheck)
                    modeComps[componentName] = tk.Checkbutton(modeGUI, 
                                                            text = componentName, 
                                                            variable = varModeCompChecks[componentName])
        

        else:
            for componentName, compPower in components.items():
                varModeCompCheck = tk.IntVar()
                varModeCompChecks[componentName] = (varModeCompCheck)
                modeComps[componentName] = tk.Checkbutton(modeGUI, 
                                                        text = componentName, 
                                                        variable = varModeCompChecks[componentName])
        
        modeCompChecks[modeNumber] = varModeCompChecks
        modeCompsRow[modeNumber] = modeComps

        modeNameLabel.grid(row = modeNumber+2, column = 0)
        modeNameEntry[modeNumber].grid(row = modeNumber+2, column = 1)  
        {modeCompsRow[modeNumber][componentName].grid(row = modeNumber+2, column = compsColumn+2) for componentName, compsColumn in zip(components, range(numberComponents))}   
   
    modeGUI.mainloop()
         
    global first
    if(first):
        compsInMode = {}  # Dict of 1's and 0's where 1 is component is used and 0 is component not used
        sameModes = False
        if(len(modes) > 0):
            sameModes = True
            for modeNumber in range(numberModes):
                if(varModeNames[modeNumber].get() != fakeModes[modeNumber].name()):
                    modes = {}
                    sameModes = False
                    break
        if(sameModes):
            compsInMode = {componentName: modeCompChecks[modeNumber][componentName].get() for componentName in components}
            modes[varModeNames[modeNumber].get()].changeComponents(components, 
                                                                compsInMode)
        else:
            for modeNumber in range(numberModes):
                compsInMode = {componentName: modeCompChecks[modeNumber][componentName].get() for componentName in components}
                modes[varModeNames[modeNumber].get()] = Mode.Mode(varModeNames[modeNumber].get(), 
                                                                components, 
                                                                compsInMode)
        
        return ModeSwitching_GUI.switching(components, 
                                        modes, 
                                        numberComponents, 
                                        numberModes)
    else: 
        return components, modes, numberComponents, numberModes