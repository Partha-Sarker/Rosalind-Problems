with open('rosalind_ba1n.txt') as file:
    pattern = list(file.readline().rstrip())
    d = int(file.readline().rstrip())


def get_neighbor(current_index, current_distance, max_d, current_pattern, neighbors):
    if current_distance >= max_d or current_index >= len(current_pattern):
        return neighbors
    new_pattern = current_pattern.copy()
    for symbol in ['A', 'C', 'G', 'T']:
        if symbol != current_pattern[current_index]:
            new_pattern[current_index] = symbol
            neighbors.append(''.join(new_pattern))
            get_neighbor(current_index + 1, current_distance + 1, max_d, new_pattern, neighbors)
    get_neighbor(current_index + 1, current_distance, max_d, current_pattern, neighbors)
    return neighbors


neighbors = get_neighbor(0, 0, d, pattern, [])
neighbors.append(''.join(pattern))
output = '\n'.join(neighbors)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
