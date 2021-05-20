from Bio.Seq import Seq


def get_pattern_count(text, pattern):
    seq = Seq(text)
    return seq.count_overlap(pattern)


with open('rosalind_ba1e.txt') as file:
    genome = file.readline().rstrip()
    k, l, t = map(lambda x: int(x), file.readline().rstrip().split(' '))


genome_len = len(genome)
clump = []

for i in range(genome_len - l + 1):
    current_genome = genome[i:i+l]
    current_genome_len = len(current_genome)
    for j in range(current_genome_len - k + 1):
        pattern = current_genome[j:j+k]
        pattern_count = get_pattern_count(current_genome, pattern)
        if pattern_count >= t and pattern not in clump:
            clump.append(pattern)
            print(pattern)
output = ' '.join(clump)
print(output)
with open('output.txt', 'w') as file:
    file.write(output)
