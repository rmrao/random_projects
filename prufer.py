import numpy as np

def t2p(input_edges):
	edges = input_edges.copy()
	verts = np.arange(edges.max() + 1)
	deg = np.zeros(len(verts))
	prufer = []
	for e in edges:
		deg[e[0]] += 1
		deg[e[1]] += 1
	while not np.sum(deg) == 2:
		v = np.where(deg == 1)[0][0]
		(row, col) = np.where(edges == v)
		row = row[0]
		col = col[0]
		prufer.append(edges[row, int(not col)])
		deg[edges[row, 0]] -= 1
		deg[edges[row, 1]] -= 1
	return prufer

