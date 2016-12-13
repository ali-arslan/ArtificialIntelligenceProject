import networkx as nx
from collections import defaultdict, deque
import threading

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
            child = next(children) # TODO Can be parallelized
            if child not in visited:
                yield parent, child
                visited.add(child)
                queue.append((child, neighbors(child)))
                # TODO Synchronisation at end of level
        except StopIteration:
            queue.popleft()

def bfs_predecessors(G, source):
    return dict((t,s) for s,t in bfs(G,source))

def bfs_successors(G, source):
    d = defaultdict(list)
    for s,t in bfs(G,source):
        d[s].append(t)
    return dict(d)

# TODO Notes: Still suboptimal 1- requires synchronisation and 2- limited bun # of nodes