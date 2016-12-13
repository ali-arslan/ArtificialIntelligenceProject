import networkx as nx
from networkx.readwrite import json_graph
import json
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import count
import threading
from multiprocessing.dummy import Pool as ThreadPool


def own_djikstra(graph, s, d):
    def _dijkstra(G, source, get_weight, pred=None, paths=None, cutoff=None,
                  target=None):
        G_succ = G.succ if G.is_directed() else G.adj

        push = heappush
        pop = heappop
        dist = {}
        seen = {source: 0}
        c = count()
        fringe = []
        push(fringe, (0, next(c), source))
        while fringe:
            (d, _, v) = pop(fringe)
            if v in dist:
                continue
            dist[v] = d
            if v == target:
                break

            for u, e in G_succ[v].items():
                cost = get_weight(v, u, e)
                if cost is None:
                    continue
                vu_dist = dist[v] + get_weight(v, u, e)
                if cutoff is not None:
                    if vu_dist > cutoff:
                        continue
                if u in dist:
                    print "L"
                elif u not in seen or vu_dist < seen[u]:
                    seen[u] = vu_dist
                    push(fringe, (vu_dist, next(c), u))
                    if paths is not None:
                        paths[u] = paths[v] + [u]
                    if pred is not None:
                        pred[u] = [v]
                elif vu_dist == seen[u]:
                    if pred is not None:
                        pred[u].append(v)

        if paths is not None:
            return dist, paths
        if pred is not None:
            return pred, dist
        return dist

    if G.is_multigraph():
        get_weight = lambda u, v, data: min(
            eattr.get(weight, 1) for eattr in data.values())
    else:
        get_weight = lambda u, v, data: data.get(weight, 1)
    l, p = _dijkstra(graph, s, get_weight)
    return p[d]

