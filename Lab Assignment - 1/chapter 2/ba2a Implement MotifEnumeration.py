with open('rosalind_ba2a.txt') as file:
    k, d = map(lambda x: int(x), file.readline().rstrip().split(' '))
    dna = list(map(lambda x: x.rstrip(), file.readlines()))


def get_hamming_distance(dna1, dna2):
    hamming_distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    return hamming_distance


def get_neighbor(current_index, current_distance, max_d, current_pattern, neighbors):
    if current_distance >= max_d or current_index >= len(current_pattern):
        return neighbors
    new_pattern = current_pattern.copy()
    for symbol in ['A', 'C', 'G', 'T']:
        if symbol != current_pattern[current_index]:
            new_pattern[current_index] = symbol
            neighbors.append(''.join(new_pattern))
            get_neighbor(current_index + 1, current_distance + 1, max_d, new_pattern, neighbors)
    get_neighbor(current_index + 1, current_distance, max_d, current_pattern, neighbors)
    return neighbors


def get_k_mers_from_dna(dna, k):
    k_mers = set()
    pattern_len = len(dna[0])
    for pattern in dna:
        for i in range(pattern_len - k + 1):
            k_mers.add(pattern[i: i+k])
    return k_mers


def appear_in_dna(dna, k_mer, hamming_distance):
    pattern_len = len(dna[0])
    for pattern in dna:
        found = False
        for i in range(pattern_len - len(k_mer) + 1):
            current_k_mer = pattern[i: i+len(k_mer)]
            if get_hamming_distance(current_k_mer, k_mer) <= hamming_distance:
                found = True
                break
        if not found:
            return False
    return True


motif_list = set()
k_mer_list = get_k_mers_from_dna(dna, k)
for k_mer in k_mer_list:
    neighbors = get_neighbor(0, 0, d, list(k_mer), [])
    neighbors.append(k_mer)
    for neighbor in neighbors:
        if neighbor in motif_list:
            continue
        if appear_in_dna(dna, neighbor, d):
            motif_list.add(neighbor)
output = ' '.join(motif_list)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)

