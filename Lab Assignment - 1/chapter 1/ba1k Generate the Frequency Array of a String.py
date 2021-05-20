import itertools

with open('rosalind_ba1k.txt') as file:
    dna = file.readline().rstrip()
    k = int(file.readline().rstrip())

limit = 4**k
symbols = ['A', 'C', 'G', 'T']

pattern_list = list(itertools.product(symbols, repeat=k))[:limit]
pattern_list = list(map(lambda x: ''.join(x), pattern_list))


def get_pattern_count(text, pattern):
    pattern_count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            pattern_count += 1
    return pattern_count


frequency = []
for pattern in pattern_list:
    frequency.append(get_pattern_count(dna, pattern))
output = ' '.join(map(lambda x: str(x), frequency))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)

