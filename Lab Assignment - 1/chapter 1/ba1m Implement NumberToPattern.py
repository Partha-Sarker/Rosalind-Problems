with open('rosalind_ba1m.txt') as file:
    index = int(file.readline().rstrip())
    k = int(file.readline().rstrip())


def number_to_pattern(index, length):
    symbol_map = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    current_pow = length - 1
    pattern = []
    for i in range(length):
        divisor = 4 ** current_pow
        symbol = symbol_map[int(index / divisor)]
        pattern.append(symbol)
        index %= divisor
        current_pow -= 1
    return ''.join(pattern)


output = number_to_pattern(index, k)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)