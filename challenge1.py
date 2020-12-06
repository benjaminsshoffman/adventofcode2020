'''Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.'''

with open('input1.txt') as f:
    lines = [int(k) for k in f.readlines()]

N = 2020
complements = set()

for entry in lines:
    complement = N - entry
    if entry in complements:
        print(entry*complement)
        break
    else:
        complements.add(complement)

print("now i'm done")