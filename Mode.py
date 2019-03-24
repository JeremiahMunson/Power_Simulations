# This row of #s is 79 characters longs,
# the maximum line length set by PEP 8 -- Style Guide for Python Code
###############################################################################

class Mode(object):
    """description of class"""

    def __init__(self, name, components, tfComponents):
        self.__Name = name
        # This is an array of the components in use in this mode,
        # filled from Comps and CompsTF
        self.__ActiveComps = []
        nothing = 0
        for componentName, compPower in components.items():
            if(tfComponents[componentName] == 1):
                self.__ActiveComps.append(componentName)
            else:
                nothing+=1
        # This had to be initialized here for some reason I believe
        self.__Requirement = "NA"
        self.__Rank = 0
        self.__BeginMode = "NA"
        self.__BeginUnits = "NA"
        self.__EndMode = "NA"
        self.__EndUnits = "NA"
        self.__Sunlight = False
        self.__Penumbra = False
        self.__Umbra = False

    # Print (1 string) the Name
    def name(self):
        return self.__Name

    # Print (1 list) the ACTIVE Components
    def components(self):
        return self.__ActiveComps

    # Reassign Components
    def changeComponents(self, components, tfComponents):
        # This is an array of the components in use in this mode, 
        # filled from Comps and CompsTF
        self.__ActiveComps = []
        nothing = 0
        for componentName, compPower in components.items():
            if(tfComponents[componentName] == 1):
                self.__ActiveComps.append(componentName)
            else:
                nothing+=1

    # Assign (1 string) when the mode is activated 
    # (random int, regular int, power, background)
    def assignRequirement(self, requirement, rank):
        self.__Requirement = requirement
        self.__Rank = rank

    # Print (1 string) when the mode is activated
    def printRequirement(self):
        return self.__Requirement

    # Print (1 int?) Mode's rank
    def printRank(self):
        return self.__Rank

    # Inputs (4 strings) Mode's Constraints 
    # (what power triggers start and stop, 
    # how frequencly of an interval and how long)
    def inputRequirementConstraints(self, beginning, beginUnits, 
                                    ending, endUnits):
        self.__BeginMode = str(beginning)
        self.__BeginUnits = str(beginUnits)
        self.__EndMode = str(ending)
        self.__EndUnits = str(endUnits)

    # Print (5 strings) Mode's Constraints
    def printReqConstraints(self):
        return [self.__Requirement, 
                self.__BeginMode, 
                self.__BeginUnits, 
                self.__EndMode, 
                self.__EndUnits]

    # Input (3 bools) what lighting conditions the mode can be on during 
    # (no imaging in umbra for example)
    def inputLightingConstraints(self, sun, penumbra, umbra):
        self.__Sunlight = sun
        self.__Penumbra = penumbra
        self.__Umbra = umbra

    # Print (3 bools) what lighting is allowed for Mode 
    def printLighting(self):
        return[self.__Sunlight, self.__Penumbra, self.__Umbra]

