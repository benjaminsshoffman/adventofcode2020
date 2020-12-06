# 2-11 n: bnplrmpvbpn
with open('input2.txt') as f:
    lines =  f.readlines()

count = 0

for entry in lines:
	rng, letter, password = entry.split()
	lower, upper = [int(k) for k in rng.split("-")]
	letter = letter.strip(":")

	letter_count = 0

	if (password[lower - 1] == letter) != (password[upper - 1] == letter):
		count += 1

print(count)
