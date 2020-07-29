d = {'A':'T','T':'A','G':'C','C':'G'}
TEMP = []
with open("059.fasta", 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        line = line.strip()
        for i in range(len(line)):
            TEMP += d[line[i]]
        TEMP = (''.join(TEMP))
print(TEMP[::-1])
