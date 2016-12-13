import networkx as nx
from networkx.readwrite import json_graph
import json
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import count
import threading
from multiprocessing.dummy import Pool as ThreadPool
import BFS



def parallel_BFS(graph, s, dest=0, paths=False):
    def checker(child, visited, queue, neighbors):
        if child not in visited:
            visited.add(child)
            queue.append((child, neighbors(child)))

    def bfs(G, source, reverse=False):
        if reverse and isinstance(G, nx.DiGraph):
            neighbors = G.predecessors_iter
        else:
            neighbors = G.neighbors_iter
        visited = set([source])
        queue = deque([(source, neighbors(source))])
        while queue: # parallelize here
            pool = ThreadPool(4)
            parent, children = queue[0]
            try:
                child = next(children)
                t = threading.Thread(target= checker, args=(child, visited, queue, neighbors)) # in parallel
                # if child not in visited:
                #     yield parent, child
                #     visited.add(child)
                #     queue.append((child, neighbors(child)))
            except StopIteration:
                queue.popleft() # synchronize

    # path = []
    # edges = list(bfs(G, s))
    # edges.reverse()
    # for x in edges:
    #     if x[1] == d:
    #         path.append(d)
    #         dest = x[0]
    #         # path.append(dest)
    # path.append(s)
    # path.reverse()
    path = []
    edges = list(own_BFS(graph, s))
    edges.reverse()
    for x in edges:
        if x[1] == dest:
            path.append(dest)
            dest = x[0]
            # path.append(dest)
    path.append(s)
    path.reverse()
    return path if paths else own_BFS(graph, s)
