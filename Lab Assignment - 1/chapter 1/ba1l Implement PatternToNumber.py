with open('rosalind_ba1l.txt') as file:
    pattern = file.readline().rstrip()


def pattern_to_number(pattern):
    symbol_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    index = 0
    current_pow = 0
    for symbol in pattern[::-1]:
        index += (symbol_map[symbol] * (4 ** current_pow))
        current_pow += 1
    return index


output = str(pattern_to_number(pattern))
print(output)
with open('output.txt', 'w') as file:
    file.write(output)