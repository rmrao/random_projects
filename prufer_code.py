import numpy as np

def t2p(input_edges):
	edges = input_edges.copy()
	deg = np.zeros(edges.max() + 1)
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
	return np.array(prufer)

def p2t(prufer):
	deg = np.array([np.sum(prufer == i) + 1 for i in range(len(prufer) + 2)])
	edges = []
	for code in prufer:
		v = np.where(deg == 1)[0][0]
		edges.append([v, code])
		deg[v] -= 1
		deg[code] -= 1
	edges.append(np.where(deg == 1)[0])
	return np.array(edges)


