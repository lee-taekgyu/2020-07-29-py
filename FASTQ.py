import sys
class FASTQ():
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_num = 0
        self.base = {}
        

    def count_line(self):
        cnt = 0
        with open(file_name , 'r') as handle:
            for line in handle:
                if cnt % 4 == 1:
                    seq = line.strip()
                    for s in seq:
                        if s in self.base:
                            self.base[s] += 1
                        else:
                            self.base[s] = 1
                cnt += 1

if __name__== "__main__":
    if len(sys.argv)!= 2:
        print(f" Usage : python {sys.argv[0]}[FASTQ]")
        sys.exit()

    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count_line()
    print(t.base)
                      
        
