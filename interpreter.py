PATH = "main.ez"

lines = []

with open(PATH, "r") as f:
    for index, value in enumerate(f.readlines()):
        lines.append(value.strip("\n"))
    lines = [i for i in lines if i] 


def operate_num(line: list) -> float:
    num_list = []
    for num in line[1:]:
        num_list.append(float(num))
    return sum(num_list)


def scan_lines(lines: list):
    for line in lines:
        split_line = line.split()
        if "output" in line:
            print(" ".join(split_line[1:]))
        if "add" in line:
            print(operate_num(split_line))


scan_lines(lines)
