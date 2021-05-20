with open('rosalind_ba3l.txt') as file:
    k, d = map(lambda x: int(x), file.readline().rstrip().split(' '))
    patterns = [pattern.rstrip() for pattern in file.readlines()]


def get_paired_fix(pattern, pre=True):
    pairs = pattern.split('|')
    pair_len = int((len(pattern) - 1) / 2)
    if pre:
        fix = '|'.join(map(lambda x: x[:pair_len-1], pairs))
    else:
        fix = '|'.join(map(lambda x: x[1:], pairs))
    return fix


def get_paired_de_bruijn_graph(patterns):
    keys, values = [], []
    graph = {}
    for pattern in patterns:
        prefix, suffix = get_paired_fix(pattern, True), get_paired_fix(pattern, False)
        keys.append(prefix)
        values.append(suffix)
        if prefix not in graph.keys():
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    for key in keys:
        if key not in values:
            first = key
            break
    for value in values:
        if value not in keys:
            last = value
            break
    graph[last] = [first]
    return graph, first, last


def get_hierholzer_cycle(adj_list, start=None):
    if start is None:
        start = next(iter(adj_list))
    stack = [start]
    cycle = []
    while len(stack) > 0:
        current_node = stack[-1]
        while len(adj_list[current_node]) != 0:
            current_node = adj_list[current_node].pop(0)
            stack.append(current_node)
        while len(stack) > 0 and len(adj_list[stack[-1]]) == 0:
            cycle.append(stack.pop())
    cycle.reverse()
    return cycle


def get_string_from_paired_cycle(cycle, d):
    string = cycle[0].split('|')[0]
    for pattern in cycle[1: d+2]:
        string += pattern.split('|')[0][-1]
    string += cycle[0].split('|')[-1]
    for pattern in cycle[1:]:
        string += pattern.split('|')[1][-1]
    return string


adjList, first, last = get_paired_de_bruijn_graph(patterns)
cycle = get_hierholzer_cycle(adjList, first)[:-1]
output = get_string_from_paired_cycle(cycle, d)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)