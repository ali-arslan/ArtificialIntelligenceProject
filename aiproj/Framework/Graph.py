# Graph implementation goes here
# most likely a wrapper around spicy: http://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html
# DO NOT ACCESS DIRECTLY! Usage via IR wrappers; apply relevant safeguards

class Graph:
    # global stack depth to define the recursion limit
    def __init__(self, nodes, edges, stackdepth):
        stackdepth
        self.nodes = nodes
        self.edges = edges

    def getNodeCount(self):
        return len(self.nodes)

    def getEdgeCount(self):
        return len(self.edges)

    def testReachibility(self):
        1
