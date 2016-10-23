# further todos...provide persistence etc.

class IntermediateRepresentation:
    # This module provides an implementation of the intermediate representation used by the framework
    # A directed acyclical graph implementation provided in Graph.py is used as the base

    # Each data load will spawn an instance and load data correspondingly
    def __init__(self, nodes, edges):
        self.graph = Graph(nodes, egdes)

    # return graph to be consumed by Algorithms
    def getGraph(self):
        return self.graph

    def getNodeCount(self):
        return len(self.graph.nodes)

    def getEdgeCount(self):
        return len(self.graph.edges)

    def testReachibility(self):
        1



