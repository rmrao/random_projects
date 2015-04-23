import numpy as np

"""Checks to see if tree is valid."""
def check_tree(edges):
	if not len(edges) or edges.min() != 0 or edges.max() != len(edges):
		return False
	seen = set()
	for edge in edges:
		if edge[0] in seen and edge[1] in seen:
			return False
		else:
			seen.add(edge[0])
			seen.add(edge[1])
	return True

"""Checks if prufer code is valid."""
def check_prufer(prufer):
	return prufer.min() >= 0 and prufer.max() <= len(prufer) + 1


"""
Input: A tree consisting of an (n, 2) numpy array of edges. Edges given by starting and ending vertex (undirected).
		Vertices should be labeled 0...n so all entries in tree should be between 0...n
Output: A numpy array for the prufer code of the tree.
"""
def t2p(input_edges):
	edges = input_edges.copy()
	if not check_tree(edges):
		raise ValueError("Input is not a valid tree")
	deg = np.zeros(len(edges) + 1)
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

"""
Input: Prufer code consisting of a numpy array of vertices.
Output: Edges of tree corresponding to prufer code.
"""
def p2t(prufer):
	if len(prufer) == 0:
		return np.array([[0, 1]])
	if not check_prufer(prufer):
		raise ValueError("Input is not valid prufer code")
	deg = np.array([np.sum(prufer == i) + 1 for i in range(len(prufer) + 2)])
	edges = []
	for code in prufer:
		v = np.where(deg == 1)[0][0]
		edges.append(sorted([v, code]))
		deg[v] -= 1
		deg[code] -= 1
	edges.append(np.where(deg == 1)[0])
	return np.array(edges)


