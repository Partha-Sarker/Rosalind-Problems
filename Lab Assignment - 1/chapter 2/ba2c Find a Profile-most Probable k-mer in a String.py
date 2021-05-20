symbol_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def get_probability(profile, pattern):
    pattern_len = len(pattern)
    probability = 1
    for i in range(pattern_len):
        probability *= profile[symbol_index[pattern[i]]][i]
    return probability


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


with open('rosalind_ba2c.txt') as file:
    text = file.readline().rstrip()
    k = int(file.readline().rstrip())
    rows = [row.rstrip() for row in file.readlines()]
    profile_matrix = []
    for row in rows:
        profile_matrix.append([float(probability) for probability in row.split(' ')])


output = get_most_probable_k_mer(profile_matrix, text, k)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
