with open('070.vcf', 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            find_ID = header.index("ID")

        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt = splitted[4]
        
        if header[find_ID] != ".":
            print(f"{chrom}, {pos}, {alt}, {ref}, {id}")
