with open('rosalind_ba1g.txt') as file:
    dna1 = file.readline().rstrip()
    dna2 = file.readline().rstrip()


def get_hamming_distance(dna1, dna2):
    len_1 = len(dna1)
    len_2 = len(dna2)
    min_len = min(len_1, len_2)
    max_len = max(len_1, len_2)
    hamming_distance = max_len - min_len

    for i in range(min_len):
        if dna1[i] != dna2[i]:
            hamming_distance += 1

    return hamming_distance


output = str(get_hamming_distance(dna1, dna2))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)