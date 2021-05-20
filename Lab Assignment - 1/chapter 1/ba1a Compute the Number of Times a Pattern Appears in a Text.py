with open('rosalind_ba1a.txt') as file:
    text = file.readline().rstrip()
    pattern = file.readline().rstrip()


def get_pattern_count(text, pattern):
    pattern_count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            pattern_count += 1
    return pattern_count


output = str(get_pattern_count(text, pattern))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)