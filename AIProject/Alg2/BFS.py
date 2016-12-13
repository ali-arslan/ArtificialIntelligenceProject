import networkx as nx
from networkx.readwrite import json_graph
import json
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import count
import threading
from multiprocessing.dummy import Pool as ThreadPool


def own_BFS(graph, s, dest=0, paths=False):
    def bfs(G, source, reverse=False):
        if reverse and isinstance(G, nx.DiGraph):
            neighbors = G.predecessors_iter
        else:
            neighbors = G.neighbors_iter
        visited = set([source])
        queue = deque([(source, neighbors(source))])
        while queue:
            parent, children = queue[0]
            try:
                child = next(children)
                if child not in visited:
                    yield parent, child
                    visited.add(child)
                    queue.append((child, neighbors(child)))
            except StopIteration:
                queue.popleft()

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
    edges = list(bfs(graph, s))
    edges.reverse()
    for x in edges:
        if x[1] == dest:
            path.append(dest)
            dest = x[0]
            # path.append(dest)
    path.append(s)
    path.reverse()
    return path if paths else bfs(graph, s)