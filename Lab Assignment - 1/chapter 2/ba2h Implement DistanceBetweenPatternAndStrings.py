with open('rosalind_ba2h.txt') as file:
    pattern = file.readline().rstrip()
    dna = file.readline().rstrip().split(' ')


def get_hamming_distance(dna1, dna2):
    dna_len = len(dna1)
    hamming_distance = 0
    for i in range(dna_len):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    return hamming_distance


def get_min_hamming_distance(text, pattern):
    min_distance = get_hamming_distance(text[:len(pattern)], pattern)
    for i in range(1, len(text) - len(pattern) + 1):
        current_pattern = text[i: i+len(pattern)]
        min_distance = min(min_distance, get_hamming_distance(current_pattern, pattern))
    return min_distance


distance = 0
for text in dna:
    distance += get_min_hamming_distance(text, pattern)
output = str(distance)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)