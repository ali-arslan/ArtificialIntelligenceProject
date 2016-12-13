import networkx as nx
from networkx.readwrite import json_graph
import json

def serialize_to_json(x):
    s = (json_graph.node_link_data(x))
    z = json.dumps(s)
    return z


def read_from_json(z):
    return json_graph.node_link_graph(json.loads(z))


def serialize_to_yaml(x, n):
    nx.write_yaml(x, n)


def read_from_yaml(z):
    return nx.read_yaml(z)