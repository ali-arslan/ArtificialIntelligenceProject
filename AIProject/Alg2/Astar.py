import networkx as nx
from networkx.readwrite import json_graph
import json
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import count
import threading
from multiprocessing.dummy import Pool as ThreadPool


def own_Astar(graph, s, d, h=None):
    def astar(G, source, target, heuristic=None, weight='weight'):
        if heuristic is None:
            def heuristic(u, v):
                return 0
        push = heappush
        pop = heappop
        c = count()
        queue = [(0, next(c), source, 0, None)]
        enqueued = {}
        explored = {}
        while queue:
            _, __, curnode, dist, parent = pop(queue)
            if curnode == target:
                path = [curnode]
                node = parent
                while node is not None:
                    path.append(node)
                    node = explored[node]
                path.reverse()
                return path
            if curnode in explored:
                continue
            explored[curnode] = parent
            for neighbor, w in G[curnode].items():
                if neighbor in explored:
                    continue
                ncost = dist + w.get(weight, 1)
                if neighbor in enqueued:
                    qcost, h = enqueued[neighbor]
                    if qcost <= ncost:
                        continue
                else:
                    h = heuristic(neighbor, target)
                enqueued[neighbor] = ncost, h
                push(queue, (ncost + h, next(c), neighbor, ncost, curnode))

    return astar(graph, s, d, h)