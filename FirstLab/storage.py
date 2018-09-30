from abc import ABC, abstractmethod


class StorageInterface(ABC):
	def __init__(self, string, basetype):
		self.init_strings = string.split('\n')
		self.vertices, self.edges = map(int, self.init_strings[0].split())
		if basetype:
			self.attached = list(map(basetype, self.init_strings[-self.vertices - 1:-1]))

	def __str__(self):
		return_string = str(self.vertices) + ' ' + str(self.edges) + '\n'
		for u in range(self.vertices):
			for v, c in self.get_adjacent(u):
				if u < v:
					return_string += str(u) + ' ' + str(v) + ' ' + str(c) + '\n'
		for u in range(self.vertices):
			return_string += str(self.attached[u]) + '\n'
		return return_string

	@abstractmethod
	def get_adjacent(self, vertex):
		pass


class Matrix(StorageInterface):
	def __init__(self, string, basetype):
		super().__init__(string, basetype)
		matrix_strings = self.init_strings[1:self.vertices + 1]
		self.matrix = []
		for u in range(self.vertices):
			self.matrix.append(list(map(int, matrix_strings[u].split())))

	def get_adjacent(self, vertex):
		return [pair for pair in zip(range(1, self.vertices + 1, 1), self.matrix[vertex - 1]) if pair[1] != 0]


class List(StorageInterface):
	def __init__(self, string, basetype):
		super().__init__(string, basetype)
		list_strings = self.init_strings[1:self.edges + 1]
		self.list = [[] for _ in range(self.vertices + 1)]
		for i in range(self.edges):
			u, v, c = map(int, list_strings[i].split())
			self.list[u].append((v, c))
			self.list[v].append((u, c))

	def get_adjacent(self, vertex):
		return self.list[vertex]
