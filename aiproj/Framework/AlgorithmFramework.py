class AlgorithmicFramework:
    # This module provides a container of all search algorithm related functionality. It follows a modular design where
    # a new instance of the framework is expected to be generated for every application

    # local variable which define common parameters for the framework
    def setGlobalStackDepth(self, stackdepth):
        self.stackDepth = stackdepth

    # global stack depth to define the recursion limit
    def __init__(self, stackdepth):
        self.stackDepth = stackdepth

