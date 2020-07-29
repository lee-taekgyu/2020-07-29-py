import sys

class FASTA():
    def __init__(self, file_name):
        self.file_name = file_name
        self.count = {}
        self.length = 0

    def count_base(self):
        with open(file_name, 'r') as handle:
            for line in handle:
                if line.startswith('>'):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1

    def count_length(self):
        for k,v in self.count.items():
            self.length += v

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage : python {sys.argv[0]}[FASTA]")
        sys.exit()

    file_name = sys.argv[1]
    t = FASTA(file_name)
    t.count_base()
    print(t.count)
    t.count_length()
    print(t.length)
