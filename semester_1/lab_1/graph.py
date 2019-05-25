from queue import Queue
from storage import Matrix, List


class Graph:
	def __init__(self, input_string, storage='list', basetype=None):
		"""
		Creates new graph

		:param input_string: string representation of graph
		:param storage: list or matrix
		:param basetype: type of values stored in nodes
		"""
		if storage == 'list':
			self.storage = List(input_string, basetype)
		elif storage == 'matrix':
			self.storage = Matrix(input_string, basetype)
		self.vertices, self.edges = self.storage.vertices, self.storage.edges

	def __str__(self):
		return str(self.storage)

	def is_connected(self):
		"""
		Check for graph connectivity via BFS

		:return: boolean value
		"""
		que = Queue()
		vis = [False] * (self.vertices + 1)
		que.put(1)
		while not que.empty():
			v = que.get()
			if not vis[v]:
				vis[v] = True
				for u, c in self.storage.get_adjacent(v):
					que.put(u)

		for v in range(1, self.vertices + 1, 1):
			if not vis[v]:
				return False
		return True

	def distance(self, fr, to):
		"""
		Count the distance between two vertices via Dijkstra algorithm

		:param fr: first vertex
		:param to: second vertex
		:return: integer value
		"""
		inf = int(1e9)
		dist = [inf] * (self.vertices + 1)
		dist[fr] = 0
		selected = [False] * (self.vertices + 1)
		for _ in range(self.vertices):
			cur_min, v = inf, 0
			for candidate in range(1, self.vertices + 1, 1):
				if not selected[candidate] and dist[candidate] <= cur_min:
					v = candidate
					cur_min = dist[candidate]
			selected[v] = True
			for u, c in self.storage.get_adjacent(v):
				if dist[v] + c < dist[u]:
					dist[u] = dist[v] + c
		return dist[to]
