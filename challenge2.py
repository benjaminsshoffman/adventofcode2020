'''Specifically, they need you to find the threee entries that sum to 2020 and then multiply those 3 numbers together.'''

with open('input1.txt') as f:
    lines = [int(k) for k in f.readlines()]

N = 2020
partial_sums = {} # maps partial sum to two numbers

for entry1 in lines:
	for entry2 in lines:
		partial_sum = entry1 + entry2
		if partial_sum > N:
			continue
		partial_sums[partial_sum] = [entry1, entry2]

for entry3 in lines:
	if N - entry3 in partial_sums:
		entry1, entry2 = partial_sums[N - entry3]
		print(entry1*entry2*entry3)

print("now i'm done")