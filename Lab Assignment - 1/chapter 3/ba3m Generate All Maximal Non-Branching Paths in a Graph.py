adjList = {}
with open('rosalind_ba3m.txt') as file:
    incoming = {}
    outgoing = {}
    while True:
        line = file.readline().rstrip()
        if line is None or line == '':
            break
        key = int(line.split('->')[0].rstrip())
        values = line.split('->')[1].rstrip().split(',')
        values = [int(value.rstrip()) for value in values]
        adjList[key] = values

        outgoing[key] = len(values)
        if key not in incoming:
            incoming[key] = 0

        for value in values:
            if value not in incoming:
                incoming[value] = 1
            else:
                incoming[value] += 1

            if value not in outgoing:
                outgoing[value] = 0


def get_incoming_outgoing(graph):
    incoming = {}
    outgoing = {}
    for key, values in graph.items():
        outgoing[key] = len(values)
        if key not in incoming:
            incoming[key] = 0

        for value in values:
            if value not in incoming:
                incoming[value] = 1
            else:
                incoming[value] += 1
            if value not in outgoing:
                incoming[value] = 0
    return incoming, outgoing


def get_maximal_non_branching_paths(graph, incoming, outgoing):
    paths = []
    for node in graph:
        if incoming[node] != 1 or outgoing[node] != 1:
            for outgoing_node in graph[node]:
                current_node = outgoing_node
                non_branching_path = [node, current_node]
                while current_node in graph and incoming[current_node] == 1 and outgoing[current_node] <= 1:
                    current_node = graph[current_node][0]
                    non_branching_path.append(current_node)
                paths.append(non_branching_path)
    visited = set()
    for path in paths:
        for node in path:
            visited.add(node)
    for node in graph:
        if node not in visited:
            current_node = node
            non_branching_path = [current_node]
            while current_node not in visited:
                visited.add(current_node)
                current_node = graph[current_node][0]
                non_branching_path.append(current_node)
            paths.append(non_branching_path)
    return paths


non_branching_paths = get_maximal_non_branching_paths(adjList, incoming, outgoing)
print(non_branching_paths)
paths = [' -> '.join(map(lambda x: str(x), path)) for path in non_branching_paths]
output = '\n'.join(paths)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)


