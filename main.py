from graph import Graph
from timedate import TimeDate

# here I decided to implement UI instead of commenting my code and clarifying what is does

storage = input('How do you want to store your graph, as matrix or as list? ')
if storage != 'list' and storage != 'matrix':
	raise ValueError('storage parameter must be list or matrix')
basetype = input('What is the type of additional data you want to append to each vertex? TimeDate? ')

print('Graph represented as a string in a following format: ')
print('N and M, Number of vertices and number of edges respectively, must be on the first line')
if storage == 'list':
	print('Then there goes M lines, each of three integers representing one edge: ids of two vertices and edge length')
elif storage == 'matrix':
	print('Then there goes N by N adjacency matrix, each non-zero value represents edge length and zero value means there is no edge')
if basetype:
	print('Finally, there must be N lines, with string representation of value associated with ith vertex in ith line')

input_string = ''
mode = input('How do you want to input your graph, from console or from file? ')
if mode == 'console':
	print('Input your graph:')
	while True:
		tmp = input()
		if tmp:
			input_string += tmp + '\n'
		else:
			break
elif mode == 'file':
	path = input('Input relative path to file with graph stored in specified format: ')
	with open(r'./' + path) as file:
		input_string = ''.join(file.readlines())
else:
	raise ValueError('mode parameter must be console or file')

g = Graph(input_string, storage, eval(basetype))

if g.is_connected():
	print('Graph is connected')
else:
	print('Graph is not connected')
u, v = map(int, input('Enter ids of vertices between which you want to calculate a distance: ').split())
print('Distance is:', g.distance(u, v))
print('Here goes your graph as a string once again:')
print(str(g))
