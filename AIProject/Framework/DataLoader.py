# This is used to load data from an input file and parse into the intermediate format before storing it in a graph

import xml.etree.ElementTree as ET #xml parser library
import json #json parser library
from pprint import pprint #json support

class DataLoader:
    # Includes parsers and transformer

    

    # assign and check input type; call appropriate parser
    def __init__(self, type):
        self.type = type
        #self.data
        self.nodes = []
        self.edges = []

        if type == "txt":
            textparser(self)
        elif type == "XML":
            XMLparser(self)
        elif type == "JSON":
            JSONparser(self)
        else
            print "File type not found!"

        #transform(self)

    # parse data and store; call transform
    def JSONparser(self):
        with open('data.json') as data_file:    
        data = json.load(data_file)

        pprint(data)


    def XMLparser(self):
        tree = ET.parse('country_data.xml')
        root = tree.getroot()
        
        #for atype in e.findall('type'): alternatively, to parse as a string
            #print(atype.get('foobar'))

    def textparser(self):
        with open("file.txt", "r") as ins:
            line = ins.readline()
            if line != "nodes":
                return False
            line = ins.readline()
            while line != "edges" && line:
                self.nodes.append(line)
                line = ins.readline()
            if line == NULL:
                return False
            line = ins.readline()
            while line:
                line_split = line.split(' ', 2)
                self.edges.append(edge(line_split[0], line_split[1], line_split[2]))
                line = ins.readline()
            return True

    # transform data to IR format and return; is expected to be piped to IntermediateRepresentation
    #DON'T NEED THIS
    def transform(self):
        1
        
