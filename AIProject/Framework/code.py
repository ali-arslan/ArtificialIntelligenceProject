import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
#G.add_node("spam")
#G.add_edge(1,2)
#G.add_node("new_spam")
#G.add_edge(1,3)
#print(list(G.nodes()))
#[1, 2, 'spam']
#print(list(G.edges()))
#[(1, 2)]

H=nx.path_graph(10)
G.add_node(H)
print(list(G.nodes()))