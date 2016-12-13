import networkx as nx
from networkx.readwrite import json_graph
import json
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import count
import threading
from multiprocessing.dummy import Pool as ThreadPool


# G.add_node("spam")
# G.add_edge(1,2)
# print(list(G.nodes()))
# print(list(G.edges()))


#






def dijisktra(self, source, dest):
    return nx.dijkstra_path(self, source, dest)


# file = open("Small.txt", "r")
# line = file.readline()  # nodes
# # print line
#
#
# for x in range(1, 6):
#     line = file.readline()
#     list1 = line.split(" ")
#     node = list1[0]
#     G.add_node(node)
# print node

# line = file.readline()  # arcs
# print line

# for x in range(1, 10):
#     line = file.readline()
#     list1 = line.split(" ")
#     e1 = list1[0]
#     e2 = list1[1]
#     weight = list1[2]
#     G.add_edge(e1, e2)


# print e1,e2,weight
# print(list(G.nodes()))
# print(list(G.edges()))
# print(list(dijisktra(G, 'LasVegas', 'SanFrancisco')))
# print(list(a_star(G, 'LasVegas', 'SanFrancisco')))
# print(list(bfs(G, 'LasVegas', 'SanFrancisco')))
# print(list(dfs(G, 'LasVegas', 'SanFrancisco')))
# print(list(dijisktra(G, 'LasVegas', 'SanFrancisco')))

# s = (json_graph.node_link_data(x))
# z = json.dumps(s)
# H = json_graph.node_link_graph(json.loads(z))





x = nx.complete_graph(1000)
print(own_DFS(x, 0))
# serialize_to_yaml(x, 'll.yaml')
# print(H)

# print(list(kruskal(G)))
