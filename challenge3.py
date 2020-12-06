# 2-11 n: bnplrmpvbpn
with open('input2.txt') as f:
    lines =  f.readlines()

count = 0

for entry in lines:
	rng, letter, password = entry.split()
	lower, upper = [int(k) for k in rng.split("-")]
	letter = letter.strip(":")

	letter_count = 0

	for l in password:
		if l == letter:
			letter_count += 1

	if letter_count <= upper and letter_count >= lower:
		count += 1

print(count)
