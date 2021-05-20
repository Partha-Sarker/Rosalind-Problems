import itertools
from Bio.Seq import Seq

with open('rosalind_ba1j.txt') as file:
    text = file.readline().rstrip()
    k, d = map(lambda x: int(x), file.readline().rstrip().split(' '))


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


def get_position_of_patterns(text, pattern, d, reverse_complement=False):
    position_list = []
    len_pattern = len(pattern)
    len_text = len(text)
    for i in range(len_text - len_pattern + 1):
        temp_pattern = text[i:i+len_pattern]
        distance = get_hamming_distance(temp_pattern, pattern)
        if distance <= d:
            position_list.append(i)
        if reverse_complement:
            distance = get_hamming_distance(temp_pattern, str(Seq(pattern).reverse_complement()))
            if distance <= d:
                position_list.append(i)
    return position_list


def freq_words_with_mismatch(text, k, d, reverse_complement=False):
    symbols = ['A', 'T', 'G', 'C']
    all_possible_patterns = list(itertools.product(symbols, repeat=k))
    freq = 0
    most_frequent_words = []
    for pattern in all_possible_patterns:
        pattern = ''.join(pattern)
        pattern_position_list = get_position_of_patterns(text, pattern, d, reverse_complement)
        pattern_count = len(pattern_position_list)
        if pattern_count > freq:
            most_frequent_words.clear()
            freq = pattern_count
            most_frequent_words.append(pattern)
        elif pattern_count == freq:
            most_frequent_words.append(pattern)
    return most_frequent_words


output = ' '.join(freq_words_with_mismatch(text, k, d, True))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
