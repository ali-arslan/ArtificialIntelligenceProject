import networkx as nx
from networkx.readwrite import json_graph
import json
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import count
import threading
from multiprocessing.dummy import Pool as ThreadPool



def own_DFS(graph, s, dest=0, paths=False):
    visited = set()

    def dfs(G, source=None):
        if source is None:
            nodes = G
        else:
            nodes = [source]
        for start in nodes:
            if start in visited:
                continue
            visited.add(start)
            stack = [(start, iter(G[start]))]
            while stack:
                parent, children = stack[-1]
                try:
                    child = next(children)
                    if child not in visited:
                        yield parent, child
                        visited.add(child)
                        stack.append((child, iter(G[child])))
                except StopIteration:
                    stack.pop()

    path = []
    edges = list(nx.dfs_edges(graph, s))
    edges.reverse()
    for x in edges:
        if x[1] == dest:
            path.append(dest)
            dest = x[0]
    path.append(s)
    path.reverse()
    return path if paths else dfs(graph, s)