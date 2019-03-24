import tkinter as tk
import Mode
import Modes_GUI
import Size_GUI

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

def comp(components, modes, numberComponents, numberModes):
    compGUI = tk.Tk()

    first = True

    def back():
        compGUI.destroy()
        # TODO: Is this a dictionary that I'm making?
        components = {varCompNames[componentNumber].get(): varCompPowers[componentNumber].get() for componentNumber in range(numberComponents)}
        Size_GUI.size(components, modes, numberComponents, numberModes)
        first = False
    
    # This is the array of the component name ENTRY BOXES. 
    compName = {}
    # This is the array of the component power ENTRY BOXES.
    compPwr = {} 
    # This is the array for the actual component name 
    # as a tkinter string variable
    varCompNames = {}
    # This is the array for the actual component power 
    # as a tkinter string variable
    varCompPowers = {} 
    
    # Making the title, column headings, and ADD and CONTINUE buttons 
    # which will always exist in the GUI
    compTitle = tk.Label(compGUI, text = "COMPONENTS")
    compNames = tk.Label(compGUI, text = "Name")
    compPwrs = tk.Label(compGUI, text = "Power (mW)")
    compGap = tk.Label(compGUI, text = "\t")

    compContinue = tk.Button(compGUI,
                            text = "CONTIUE", 
                            command = compGUI.destroy)

    compBack = tk.Button(compGUI,
                        text = "BACK",
                        command = compGUI.destroy)
    
    # Title and column headings will always be the same so I put 
    # in the grid for them here to clear up later on
    compTitle.grid(row = 0, column = 0, columnspan = 3)
    compNames.grid(row = 1, column = 1)
    compPwrs.grid(row = 1, column = 2)
    compGap.grid(row = numberComponents + 3, column = 0)
    compContinue.grid(row = numberComponents + 4, column = 0, columnspan = 3, sticky = tk.W + tk.E)
    #compBack.grid(row = numberComponents + 5, column = 0, columnspan = 3, sticky = tk.W + tk.E)
    
    for componentNumber in range(numberComponents):
            # Making component name variable and component power variable.
            # Must be done in the loop because the program needs a new 
            # variable for each row/component otherwise they'd be the 
            # same for each component
            varCompName = tk.StringVar()
            varCompName.set("Comp"+str(componentNumber + 1))
            # To keep track of each component
            varCompNames[componentNumber] = varCompName
            varCompPower = tk.StringVar()
            varCompPower.set(0)
            # To keep track of each component
            varCompPowers[componentNumber] = varCompPower
    
            # Making the Label and Entry's for each row/component using 
            # varCompNames and varCompPowers. 
            # Using varCompNames[i] and varCompPowers[i] is necessary so 
            # proper variables are updated with user input and can be 
            # accessed later.
            comp = tk.Label(compGUI, 
                            text = "Comp " + str(componentNumber + 1))

            compName[componentNumber] = tk.Entry(compGUI, 
                                textvariable = varCompNames[componentNumber])
            
            compPwr[componentNumber] = tk.Entry(compGUI, 
                                textvariable = varCompPowers[componentNumber])

            comp.grid(row = componentNumber + 2, column = 0)

            compName[componentNumber].grid(row = componentNumber + 2,
                                        column = 1)

            compPwr[componentNumber].grid(row = componentNumber + 2, 
                                        column = 2)
    
###############################################################################
            
    compGUI.mainloop()

    if(first):
        # TODO: Again, what exactly is this doing?
        components = {varCompNames[componentNumber].get(): varCompPowers[componentNumber].get() for componentNumber in range(numberComponents)}
        return Modes_GUI.mode(components, modes, numberComponents, numberModes)