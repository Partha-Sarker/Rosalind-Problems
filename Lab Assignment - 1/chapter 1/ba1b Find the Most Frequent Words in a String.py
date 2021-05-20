from Bio.Seq import Seq

with open('rosalind_ba1b.txt') as file:
    text = file.readline().rstrip()
    k = int(file.readline().rstrip())


def get_pattern_count_dict(text, length=3):
    pattern_dict = {}
    seq = Seq(text)
    for i in range(len(text) - length + 1):
        pattern = text[i:i + length]
        if pattern in pattern_dict:
            continue
        count = seq.count_overlap(pattern)
        pattern_dict[pattern] = count
    return pattern_dict


def get_most_freq_patterns(text, length=3):
    dict = get_pattern_count_dict(text, length)
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    most_frequent_k_mers = [dict[0][0]]
    for i in range(1, len(dict)):
        if dict[i][1] != dict[i - 1][1]:
            break
        most_frequent_k_mers.append(dict[i][0])

    return most_frequent_k_mers


k_mers = get_most_freq_patterns(text, k)
output = ' '.join(k_mers)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)