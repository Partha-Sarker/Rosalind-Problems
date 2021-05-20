with open('rosalind_ba3g.txt') as file:
    adjList = {}
    while True:
        line = file.readline().rstrip()
        if line is None or line == '':
            break
        key = int(line.split('->')[0].rstrip())
        values = line.split('->')[1].rstrip().split(',')
        values = [int(value) for value in values]
        adjList[key] = values


def connect_and_get_first(adj_list):
    incoming = {}
    outgoing = {}
    for key, values in adj_list.items():
        incoming[key] = len(values)
        if key not in outgoing:
            outgoing[key] = 0
        for value in values:
            if value not in outgoing:
                outgoing[value] = 1
            else:
                outgoing[value] += 1
            if value not in incoming:
                incoming[value] = 0
    incoming = dict(sorted(incoming.items()))
    outgoing = dict(sorted(outgoing.items()))
    for key in incoming.keys():
        if incoming[key] > outgoing[key]:
            first = key
        elif incoming[key] < outgoing[key]:
            last = key
    if last not in adj_list:
        adj_list[last] = [first]
    else:
        adj_list[last].append(first)
    return first


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


first = connect_and_get_first(adjList)
euler_path = get_hierholzer_cycle(adjList, first)[0: -1]
output = '->'.join([str(node) for node in euler_path])
print(output)
with open('output.txt', 'w') as file:
    file.write(output)