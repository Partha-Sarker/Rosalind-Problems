import itertools


def get_hamming_distance(dna1, dna2):
    dna_len = len(dna1)
    hamming_distance = 0

    for i in range(dna_len):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    return hamming_distance


def get_text_distance(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    min_distance = pattern_len

    for i in range(text_len-pattern_len+1):
        temp_pattern = text[i:i+pattern_len]
        distance = get_hamming_distance(temp_pattern, pattern)
        if min_distance > get_hamming_distance(temp_pattern, pattern):
            min_distance = distance
    return min_distance


def get_dna_distance(dna, pattern):
    distance = 0
    for text in dna:
        text_distance = get_text_distance(text, pattern)
        distance += text_distance
    return distance


with open('rosalind_ba2b.txt') as file:
    k = int(file.readline().rstrip())
    dna = [pattern.rstrip() for pattern in file.readlines()]

symbols = 'GACT'
all_patterns = list(itertools.product(symbols, repeat=k))
min_distance = k*len(dna)
median = ''
for pattern in all_patterns:
    pattern = ''.join(pattern)
    distance = get_dna_distance(dna, pattern)
    if min_distance > distance:
        min_distance = distance
        median = pattern
output = median
print(output)
with open('output.txt', 'w') as file:
    file.write(output)

