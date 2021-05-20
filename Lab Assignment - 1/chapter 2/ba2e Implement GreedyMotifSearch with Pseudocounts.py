import numpy as np

symbol_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def get_profile_from_motifs(motifs, pseudo_count=True):
    k = len(motifs[0])
    t = len(motifs)
    count = 0.0
    if pseudo_count:
        count = 1.0
    profile = [[count]*k, [count]*k, [count]*k, [count]*k]
    for text in motifs:
        for i in range(k):
            index = symbol_index[text[i]]
            profile[index][i] += 1
    divisor = t
    if pseudo_count:
        divisor += 4
    np_profile = np.array(profile)/divisor
    profile = np_profile.tolist()
    return profile


def get_probability(profile, pattern):
    pattern_len = len(pattern)
    probability = 1
    for i in range(pattern_len):
        probability *= profile[symbol_index[pattern[i]]][i]
    return probability


def get_score_from_motifs(motifs):
    t = len(motifs)
    motif_len = len(motifs[0])
    score = 0
    for i in range(motif_len):
        count = {}
        best_count = 0
        for motif in motifs:
            symbol = motif[i]
            if symbol not in count.keys():
                count[symbol] = 1
            else:
                count[symbol] += 1
            if count[symbol] > best_count:
                best_count = count[symbol]
        score += (t-best_count)
    return score


def get_most_probable_k_mer(profile, text, k):
    most_probable_k_mer = ''
    max_probability = -1
    text_len = len(text)
    for i in range(text_len - k + 1):
        pattern = text[i:i + k]
        probability = get_probability(profile, pattern)
        if probability > max_probability:
            max_probability = probability
            most_probable_k_mer = pattern
    return most_probable_k_mer


def greedy_motif_search(dna, k, t):
    best_motifs = [text[:k] for text in dna]
    best_score = get_score_from_motifs(best_motifs)
    text_len = len(dna[0])
    for i in range(text_len-k+1):
        current_motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            current_profile = get_profile_from_motifs(current_motifs)
            most_probable_pattern = get_most_probable_k_mer(current_profile, dna[j], k)
            current_motifs.append(most_probable_pattern)
        current_score = get_score_from_motifs(current_motifs)
        if current_score < best_score:
            best_motifs = current_motifs
            best_score = current_score
    return best_motifs


with open('rosalind_ba2e.txt') as file:
    k, t = map(lambda x: int(x), file.readline().rstrip().split(' '))
    dna = [pattern.rstrip() for pattern in file.readlines()]


best_motifs = greedy_motif_search(dna, k, t)
output = '\n'.join(best_motifs)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)