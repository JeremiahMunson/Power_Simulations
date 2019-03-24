## These Power Simulations were created by Jeremiah Munson (Carthage '19) for the CaNOP CubeSat
import tkinter as tk
import Mode
from Input_GUI import Size_GUI, File_Input, Battery_GUI

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

components = {} ## List of component objects
modes = {} ## Dict of mode objects

## I need to know if the user will do a manual input or import a spreadsheet
## I need to make a gui to ask because this is a sophisticated program haha
inputGUI = tk.Tk()
# This is an integer because if I do a BooleanVar
# it'll have one button preclicked, this way it won't
varFileOverManual = tk.IntVar()
# This makes sure neither button is pressed automatically
varFileOverManual.set(3) 
inputTitle = tk.Label(inputGUI,
                    text = "Would you like to input the mission data manually or through a file?")

fileButton = tk.Radiobutton(inputGUI,
                            text = "File Input", 
                            variable = varFileOverManual, 
                            value = 1, 
                            indicatoron = 0, 
                            command = inputGUI.destroy)

manualButton = tk.Radiobutton(inputGUI, 
                            text = "Manual Input", 
                            variable = varFileOverManual, 
                            value = 0, 
                            indicatoron = 0, 
                            command = inputGUI.destroy)

inputTitle.grid(row = 0, column = 0, columnspan = 2)
fileButton.grid(row = 1, column = 0, sticky = tk.W + tk.E)
manualButton.grid(row = 1, column = 1, sticky = tk.W + tk.E)

inputGUI.mainloop()

# This runs the code to grab from a file if the user chose that option 
# otherwise it runs the code for manual input if that was chosen
if (varFileOverManual.get()):
    components, modes, numberComponents, numberModes = File_Input.run(components, modes)

elif(varFileOverManual.get() == False):
    # This runs the GUI input for manual entry and sets the components to 
    # a list of Component objects, modes to a list of Mode objects, 
    # numberComponents to the number of components + 1, 
    # and numberModes to the number of modes + 1
    components, modes, numberComponents, numberModes = Size_GUI.size(components, modes)

else:
    print("ERROR GETTING USER INFORMATION")



### THE FOLLOWING IS TO PRINT OFF THE RESULTS OF THE INPUT TO ENSURE I WROTE THE PROGRAM CORRECTLY ###

print("There are {} components...".format(numberComponents))
for componentName, compPower in components.items():
    print(componentName + ":", compPower, "mW") 
print("\n")

print("There are {} modes...".format(numberModes))
for name,mode in modes.items():
    strPrint = name + ": "
    for index in range(len(mode.components())):
        strPrint += mode.components()[index] + ", "
    #for j in range(len(mode.components())):
    #    strPrint += (mode.components()[j].name() + ", ")
    strPrint = strPrint[0:(len(strPrint) - 2)]
    print(strPrint)
print("\n")

print("Power Draw...")
for name,mode in modes.items():
    modePowerPrint = name + ":"
    draw = 0
    for j in range(len(mode.components())):
        draw+=int(components[mode.components()[j]])
    print(modePowerPrint, draw, "mW")
print("\n")

print("Mode Requirements and Rank...")
for name,mode in modes.items():
    SOMETHING = mode.printReqConstraints()
    requirement =  SOMETHING[0]
    begin       =  SOMETHING[1]
    beginUnits  =  SOMETHING[2]
    end         =  SOMETHING[3]
    endUnits    =  SOMETHING[4]
    print(name + ":",  
        str(requirement), 
        mode.printRank(),  
        "triggered", 
        str(begin),  
        str(beginUnits), 
        "and lasting until", 
        str(end), 
        str(endUnits))

print("\n")

print("Mode Lighting Requirements...")
for name,mode in modes.items():
    lightingString = name + ":"
    if(mode.printLighting()[0] == True):
        lightingString+= " Sunlight,"
    if(mode.printLighting()[1] == True):
        lightingString+=" Shade,"
    if(mode.printLighting()[2] == True):
        lightingString+=" Darkness,"
    lightingString = lightingString[0:(len(lightingString) - 1)]
    print(lightingString)


''' GETTING SIMULATION FILE '''
batterySize, batteryStart, battStartWhr, timeStep = Battery_GUI.runGUI()

''' ACTUAL SIMULATIONS '''


