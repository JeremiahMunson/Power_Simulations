import tkinter as tk
import Mode
import Size_GUI
import Components_GUI
import Modes_GUI
import ModeSwitching_GUI
import Constraints_GUI
import Lighting_GUI

def run(components, modes):

    # Get number of components and number of modes from user
    components, modes, numberComponents, numberModes = Size_GUI.size(components, modes)
    # Get component names and power draws
    #components = Components_GUI.comp(components, modes, numberComponents, numberModes)
    # Get mode names and active components
    #modes = Modes_GUI.mode(components, modes, numberComponents, numberModes)
    # Get information about what triggers a mode and the mode ranks
    #modes = ModeSwitching_GUI.switching(components, modes, numberComponents, numberModes)
    # Get General Constraints
    #modes = Constraints_GUI.constraint(components, modes, numberComponents, numberModes)
    # Get Lighting Constraints
    #modes = Lighting_GUI.lighting(components, modes, numberComponents, numberModes)

    return (components, modes, numberComponents, numberModes)