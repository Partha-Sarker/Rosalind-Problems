patterns = []
with open('rosalind_ba3k.txt') as file:
    lines = file.readlines()
    patterns = [pattern.rstrip() for pattern in lines]


def get_de_bruijn_graph(patterns):
    keys, values = [], []
    graph = {}
    for pattern in patterns:
        prefix, suffix = pattern[:-1], pattern[1:]
        keys.append(prefix)
        values.append(suffix)
        if prefix not in graph.keys():
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    return graph


def path_degrees(graph):
    indegree = {}
    outdegree = {}

    for source in graph:
        if source not in indegree:
            indegree[source] = 0
        outdegree[source] = len(graph[source])
        for sink in graph[source]:
            if sink in indegree:
                indegree[sink] += 1
            else:
                indegree[sink] = 1
            if sink not in outdegree:
                outdegree[sink] = 0

    return indegree, outdegree


def find_contigs(graph, node, indegree, outdegree):
    contigs = []
    for next in graph[node]:
        new_path = [node, next]
        ins, outs = indegree[next], outdegree[next]
        while ins == 1 and outs == 1:
            node = next
            next = graph[node][0]
            new_path.append(next)
            ins, outs = indegree[next], outdegree[next]
        contigs.append(new_path)
    return contigs


def debruijn_to_contigs(graph):
    outpaths = []
    indegree, outdegree = path_degrees(graph)
    for node in outdegree:
        ins, outs = indegree[node], outdegree[node]
        if outs > 0 and not (outs == 1 and ins == 1):
            outpaths.extend(find_contigs(graph, node, indegree, outdegree))
    return outpaths


def get_string_from_path(path):
    string = path[0]
    for pattern in path[1:]:
        string += pattern[-1]
    return string


graph = get_de_bruijn_graph(patterns)
paths = debruijn_to_contigs(graph)
contigs = []
for path in paths:
    contigs.append(get_string_from_path(path))
output = ' '.join(contigs)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)