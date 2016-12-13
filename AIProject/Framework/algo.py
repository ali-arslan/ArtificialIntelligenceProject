

def dijisktra(self,source,dest):
	return nx.dijkstra_path(self,source,dest)

def a_star(self,soucre,dest,heuristic):
 	return nx.astar_path(self,soucre,dest,heuristic)

def bfs(self,source):
	return list(nx.bfs_edges(G,source))

def kruskal(self)
	mst = tree.minimum_spanning_edges(G, algorithm='kruskal', data=False)
	edgelist = list(mst)
	return sorted(edgelist)	
