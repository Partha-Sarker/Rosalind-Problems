with open('rosalind_ba1d.txt') as file:
    pattern = file.readline().rstrip()
    genome = file.readline().rstrip()


def get_pattern_locations(text, pattern):
    locations = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            locations.append(i)
    return locations


locations = get_pattern_locations(genome, pattern)
output = ' '.join(map(lambda x: str(x), locations))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)