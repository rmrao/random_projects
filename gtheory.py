import numpy as np

def check_input(game, rbeliefs, cbeliefs):
	if rbeliefs is None:
		rbeliefs = np.ones(game.shape[1])
	elif np.isscalar(rbeliefs):
		rbeliefs = np.ones(game.shape[1])*rbeliefs
	elif not isinstance(rbeliefs, np.ndarray) or rbeliefs.shape != (game.shape[1],):
		raise ValueError("Incorrect input for rbeliefs")
	if cbeliefs is None:
		cbeliefs = np.ones(game.shape[0])
	elif np.isscalar(cbeliefs):
		cbeliefs = np.ones(game.shape[0])*cbeliefs
	elif not isinstance(cbeliefs, np.ndarray) or cbeliefs.shape != (game.shape[0],):
		raise ValueError("Incorrect input for cbeliefs")
	return rbeliefs, cbeliefs


def play(game, rbeliefs=None, cbeliefs=None):
	if isinstance(rbeliefs, list):
		rbeliefs = map(float, rbeliefs)
		rbeliefs = np.array(rbeliefs)
	if isinstance(cbeliefs, list):
		cbeliefs = map(float, cbeliefs)
		cbeliefs = np.array(cbeliefs)
	game = np.matrix(game)
	rbeliefs, cbeliefs = check_input(game, rbeliefs, cbeliefs)
	for i in range(100):
		rprobs = np.matrix(rbeliefs/np.sum(rbeliefs)).T
		cprobs = np.matrix(cbeliefs/np.sum(cbeliefs))
		rmove = np.argmax(game*rprobs)
		cmove = np.argmin(cprobs*game)
		rbeliefs[cmove] += 1
		cbeliefs[rmove] += 1
		print "Game value = ", game[rmove, cmove]
	print rbeliefs, cbeliefs
