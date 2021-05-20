with open('rosalind_ba1h.txt') as file:
    pattern = file.readline().rstrip()
    text = file.readline().rstrip()
    d = int(file.readline().rstrip())


def get_hamming_distance(pattern1, pattern2):
    len_1 = len(pattern1)
    len_2 = len(pattern2)
    min_len = min(len_1, len_2)
    max_len = max(len_1, len_2)
    hamming_distance = max_len - min_len

    for i in range(min_len):
        if pattern1[i] != pattern2[i]:
            hamming_distance += 1
    return hamming_distance


locations = []
for i in range(len(text) - len(pattern) + 1):
    current_pattern = text[i: i + len(pattern)]
    if get_hamming_distance(current_pattern, pattern) <= d:
        locations.append(i)

output = ' '.join(map(lambda x: str(x), locations))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)