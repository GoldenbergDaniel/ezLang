PATH = "main.ez"

lines = []

with open(PATH, "r") as f:
    for index, value in enumerate(f.readlines()):
        lines.append(value.strip("\n"))
    lines = [i for i in lines if i] 


def scan_lines(lines: list):
    for line in lines:
        if "print" in line:
            split_line = line.split()
            print(" ".join(split_line[1:]))
        if "add" in line:
            split_line = line.split()
            num_list = []
            for num in split_line[1:]:
                num_list.append(int(num))
            print(sum(num_list))


scan_lines(lines)
