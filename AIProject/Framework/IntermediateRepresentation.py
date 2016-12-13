# further todos...provide persistence etc.

class IntermediateRepresentation:
    # This module provides an implementation of the intermediate representation used by the framework
    # A directed acyclical graph implementation provided in Graph.py is used as the base

    # Each data load will spawn an instance and load data correspondingly
    def __init__(self, nodes, edges):
        self.graph = Graph(nodes, egdes)

    # return graph to be consumed by Algorithms
    def getGraph(self):
        return self.graph.G

    def getNodeCount(self):
        return len(self.graph.G)

    def getEdgeCount(self):
        return self.graph.G.number_of_edges()

    def testReachibility(self):
        return self.graph.testReachibility()



