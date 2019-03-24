import tkinter as tk
import Mode
from Input_GUI import Constraints_GUI

# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

def lighting(components, modes, numberComponents, numberModes):
    lightingGUI = tk.Tk()

    #first = True

    def back():
        lightingGUI.destroy()
        for modeName, mode in modes.items():
            mode.inputLightingConstraints(lightingCheckVals[modeName][0].get(), 
                                        lightingCheckVals[modeName][1].get(), 
                                        lightingCheckVals[modeName][2].get())

        Constraints_GUI.constraint(components, 
                                modes, 
                                numberComponents, 
                                numberModes)
        #first = False

    lightingTitle = tk.Label(lightingGUI, 
                            text = "SUNLIGHT/SHADE REQUIREMENTS")

    lightingModesHead = tk.Label(lightingGUI, text = "Modes")
    lightingSun = tk.Label(lightingGUI, text = "On in Sunlight")
    lightingPenumbra = tk.Label(lightingGUI, text = "On in Penumbra")
    lightingUmbra = tk.Label(lightingGUI, text = "On in Umbra")
    lightingGap = tk.Label(lightingGUI, text = "\t")

    lightingFinish = tk.Button(lightingGUI,
                            text = "FINISH", 
                            command = lightingGUI.destroy)

    #Constraints_GUI.constraint(components, modes, numberComponents, numberModes))
    lightingBack = tk.Button(lightingGUI, text = "BACK", command = back)

    lightingTitle.grid(row = 0, column = 0, 
                    columnspan = 4, sticky = tk.W + tk.E)

    lightingModesHead.grid(row = 1, column = 0)
    lightingSun.grid(row = 1, column = 1)
    lightingPenumbra.grid(row = 1, column = 2)
    lightingUmbra.grid(row = 1, column = 3)
    lightingGap.grid(row = numberModes + 3, column = 0)

    lightingFinish.grid(row = numberModes + 4, column = 0, 
                    columnspan = 4, sticky = tk.W + tk.E)

    lightingBack.grid(row = numberModes + 5, column = 0, 
                    columnspan = 4, sticky = tk.W + tk.E)
    
    lightingModes = {}
    lightingCheckVals = {}
    lightingChecks = {}

    LIGHTING_OPTIONS = {
        "Sunlight": "Sunlight",
        "Shade": "Penumbra",
        "Darkness": "Umbra"
        }

    for (modeName, mode), lightingRow in zip(modes.items(), range(numberModes)):
        varLighting = {}
        lights = {}
        lights[0], lights[1], lights[2] = mode.printLighting()

        lightingModes[modeName] = (tk.Label(lightingGUI, text = modeName))
        lightingModes[modeName].grid(row = lightingRow + 2, column = 0)

        for text, index in zip(LIGHTING_OPTIONS, range(len(LIGHTING_OPTIONS))):
            varLighting[index] = tk.BooleanVar()
            varLighting[index].set(lights[index])

            lightingChecks[index] = tk.Checkbutton(lightingGUI,
                                                text=text, 
                                                variable=varLighting[index])

            lightingChecks[index].grid(row = lightingRow + 2, column = index + 1)
            
        lightingCheckVals[modeName] = varLighting

    lightingGUI.mainloop()

    for modeName, mode in modes.items():
        mode.inputLightingConstraints(lightingCheckVals[modeName][0].get(), 
                                    lightingCheckVals[modeName][1].get(),
                                    lightingCheckVals[modeName][2].get()) 

    return components, modes, numberComponents, numberModes