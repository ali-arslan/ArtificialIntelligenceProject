from django.shortcuts import render
from django.http import HttpResponse
import networkx as nx
from django.http import JsonResponse
import Alg2.BFS
import Alg2.DFS
import Alg2.Djikstra
import Alg2.Astar
import Alg2.ParallelBFS
import Alg2.Parsers

# Start from a root, and visit all the
# connected nodes in a graph
#  Nodes closer to the root are visited first
#  Nodes of the same hop-distance (level)
# from the root can be visited in parallel

def uploadData():
    i = 9



def index(request):
    G = ''
    h = ''
    upload = ''

    # All the Django code that needs to be understood is here.
    # Just get relevant parameters here and run if-else block.
    # Run searches and return result as JSON (also shown below)







    testgraphtype = request.GET.get('generate', 'NOP')  # if generating graph
    nodecount = int(request.GET.get('nodecount', '10'))  # number of nodes for generated graph
    graphupload = request.GET.get('upload', 'NOP')  # if uploading graph
    sp = int(request.GET.get('startingpoint', '0'))  # starting point for routing
    dp = int(request.GET.get('destpoint', '0'))  # starting point for routing
    traversaltype = request.GET.get('traversaltype', 'NOP')   # traversal type [simpDFS, simpBFS, MST, Kruskals, optDFS, parallelBFS]

    if testgraphtype == 'complete':  # generate or build graph appropriately
        G = nx.complete_graph(nodecount)
    if graphupload == 'yes':
        G = uploadData()

    if traversaltype == 'simple_bfs':  # determine appropriate traversal and call code for it
        h = list(nx.bfs_edges(G, sp))
    elif traversaltype == 'simple_dfs':
        h = list(nx.bfs_edges(G, sp))
    elif traversaltype == 'mst':
        h = list(nx.bfs_edges(G, sp))
    elif traversaltype == 'djikstra':
        h = list(nx.bfs_edges(G, sp))
    elif traversaltype == 'optimized_dfs':
        h = list(nx.bfs_edges(G, sp))
    elif traversaltype == 'parallelized_bfs':
        h = list(nx.bfs_edges(G, sp))
    else:
        h = list(nx.bfs_edges(G, sp))



    print(h)  # for debugging
    return JsonResponse({'foo':h})  # retrn result as JSON

# Create your views here.
