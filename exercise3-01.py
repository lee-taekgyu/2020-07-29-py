import sys
import json

count ={}   
def count_base(file_name):
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith('>'):
                continue
            line = line.strip()
            for s in line:
                if s in count:
                    count[s] += 1
                else:
                    count[s] = 1
print(count)
   
def to_json(count, file_name):
    with open("switch_to_json", 'w') as handle:
        json.dump(count, handle, indent =4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#Usage : python {sys.argv[0]}[txt]")
        sys.exit()

    file_name = sys.argv[1]
