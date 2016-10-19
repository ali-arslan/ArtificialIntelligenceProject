# This is used to load data from an input file and parse into the intermediate format before storing it in a graph

class DataLoader:
    # Includes parsers and transformer

    # assign and check input type; call appropriate parser
    def __init__(self, type):
        self.type = type
        self.data

    # parse data and store; call transform
    def JSONparser(self):
        1

    def XMLparser(self):
        1

    def textparser(self):
        1

    # transform data to IR format and return; is expected to be piped to IntermediateRepresentation
    def transform(self):
        1
