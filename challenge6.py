# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
from functools import reduce

# how many trees on these slope????

with open("input3.txt") as f:
	M = [line.strip() for line in f.readlines()]

width = len(M[0])
height = len(M)

print(width, height)

def get_trees(right, down):
	hops = [(k, int(right*k/down) % width) for k in range(0, height, down)]

	count = 0

	for ypos, xpos in hops:
		print(ypos, xpos)
		if M[ypos][xpos] == '#':
			count +=1
	return count

slopes = [
		[1, 1],
		[3, 1],
		[5, 1],
		[7, 1],
		[1, 2]
	]

tree_counts = [get_trees(s[0], s[1]) for s in slopes]
print(tree_counts)


print(reduce(lambda x, y: x*y, [get_trees(s[0], s[1]) for s in slopes]))		