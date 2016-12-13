# Graph implementation goes here
# most likely a wrapper around spicy: http://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html
# DO NOT ACCESS DIRECTLY! Usage via IR wrappers; apply relevant safeguards

import networkx as nx

class Graph:
    # global stack depth to define the recursion limit
    def __init__(self, nodes, edges, stackdepth):
        stackdepth

        self.G = x.Graph()
        self.G.add_nodes_from(nodes)
        for edge in edges:
        	self.G.add_edge(edge.first,edge.second,{‘weight’:edge.weight})

    def getNodeCount(self):
        return len(self.G)

    def getEdgeCount(self):
        return self.G.number_of_edges()

    def testReachibility(self):
        if len(self.G.descendants( self.G.nodes()[0]))+1 == getNodeCount:
        	return True
        else
        	return False
