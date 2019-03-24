import tkinter as tk
import os
import sys
import Mode
import pandas as pd

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

import warnings
warnings.filterwarnings('ignore') 
# Cuts out the 
# "A value is try to be set to a copy of a slice of a dataframe"
# or something like that
# Errors still come through

def run(components, modes):
    location = "C:\\Users\...\\testFile2.csv"

    def cancel():
        print("Program Terminated")
        sys.exit()

    first = True
    
    while(True):
        fileGUI = tk.Tk()
    
        varLocation = tk.StringVar()

        # \t is tab so \testFile -> \t estFile but \\testFile -> \testFile
        varLocation.set(location) 
    
        # A GUI that doesn't change size or anything, this is so nice
        fileTitle = tk.Label(fileGUI, text = "Input File Location")
        locationEntry = tk.Entry(fileGUI, textvariable = varLocation)
        errorTxt = "Could not find file at " + location
        locationError = tk.Label(fileGUI, text = errorTxt)

        fileContinue = tk.Button(fileGUI, text = "CONTINUE", 
                                command = fileGUI.destroy)

        fileCancel = tk.Button(fileGUI, text = "CANCEL",
                            command = cancel)
    
        fileTitle.grid(row = 0, column = 0, 
                    columnspan = 5,  sticky = tk.W + tk.E)

        locationEntry.grid(row = 1, column = 0, 
                        columnspan = 5, sticky = tk.W + tk.E)

        if(not first):
            locationError.grid(row = 2, column = 0, 
                            columnspan = 5, sticky = tk.W + tk.E)

        fileContinue.grid(row = 3, column = 0, 
                        columnspan = 5, sticky = tk.W + tk.E)
        
        fileCancel.grid(row = 4, column = 0,
                        columnspan = 5, sticky = tk.W + tk.E)

        fileGUI.mainloop()

        location = varLocation.get()

        if(os.path.exists(location)):
            break
        else:
            first = False


    input = pd.read_csv(location)
    # Spliting the Spreadsheet into two dataframes: 
    # 1 for components, 1 for modes
    # Components Dataframe
    component = (input['Object'] == "Component")
    comps = input[component]
    # Only care about component name and power
    comps = comps[comps.columns[[1,2]]] 
    comps.rename(columns={'Power/Comp1':'Power'}, inplace=True)
    # Modes Dataframe
    mode = (input['Object'] == "Mode")
    mods = input[mode]
    mods.rename(columns = {"Power/Comp1":"Comp1"}, inplace=True)

    for i in range(len(comps)):
        components[comps['Name'].iloc[i]] = comps['Power'].iloc[i]

    def checkModes(componentsDict, modsDF, modeNumber):
        tfComponents = {}
        for componentName, compPower in components.items():
            tfComponents[componentName] = 0
        for i in range(len(components)):
            compHeading = "Comp"+str(i+1)
            tfComponents[modsDF[compHeading].iloc[modeNumber]] = 1

        return tfComponents

    for i in range(len(mods)):
        tfComps = {}
        tfComps = checkModes(components, mods, i)
        key = mods['Name'].iloc[i]
        modes[key] = Mode.Mode(mods['Name'].iloc[i], 
                                                components, 
                                                tfComps)

        modes[key].assignRequirement(mods['Requirement'].iloc[i], 
                                    mods['Rank'].iloc[i])

        #modes[mods['Name'].iloc[i]].inputRank(mods['Rank'].iloc[i])

        modes[key].inputRequirementConstraints(mods['Begin'].iloc[i], 
                                            mods['BeginUnits'].iloc[i],
                                            mods['End'].iloc[i], 
                                            mods['EndUnits'].iloc[i])
                                                            
        modes[key].inputLightingConstraints(mods['Sunlight'].iloc[i], 
                                            mods['Penumbra'].iloc[i], 
                                            mods['Umbra'].iloc[i])


    return components, modes, len(comps), len(mods)