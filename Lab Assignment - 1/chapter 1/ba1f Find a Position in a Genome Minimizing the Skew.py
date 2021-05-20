import numpy as np

with open('rosalind_ba1f.txt') as file:
    dna = file.readline().rstrip()

skew_map = {'C': -1, 'G': 1, 'T': 0, 'A': 0}
skew = np.empty(len(dna), dtype=np.int16)
count = 0
for i, char in enumerate(dna):
    count += skew_map[char]
    skew[i] = count

min_skew = min(skew)
indices = np.where(skew == min_skew)[0] + 1
output = ' '.join(map(lambda x: str(x), indices))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
