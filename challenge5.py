# how many trees on the right-3 down-1 slope????

with open("input3.txt") as f:
	M = [line.strip() for line in f.readlines()]

width = len(M[0])
height = len(M)

hops = [3*k % width for k in range(height)]

count = 0

for ypos, xpos in enumerate(hops):
	if M[ypos][xpos] == '#':
		count +=1

print(count)		