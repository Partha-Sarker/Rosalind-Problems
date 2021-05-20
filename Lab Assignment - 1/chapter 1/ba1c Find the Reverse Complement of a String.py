from Bio.Seq import Seq

with open('rosalind_ba1c.txt') as file:
    pattern = file.readline().rstrip()

output = str(Seq(pattern).reverse_complement())
print(output)
with open('output.txt', 'w') as file:
    file.write(output)