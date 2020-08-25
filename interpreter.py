PATH = "main.ez"

lines = []

with open(PATH, "r") as f:
  for index, value in enumerate(f.readlines()):
    lines.append(value.strip("\n"))
  lines = [i for i in lines if i] 


def operate_num(line: list) -> float:
  if line[2] == "+":
    return float(line[1]) + float(line[3])
  if line[2] == "-":
    return float(line[1]) - float(line[3])
  if line[2] == "*":
    return float(line[1]) * float(line[3])
  if line[2] == "/":
    return float(line[1]) / float(line[3])
  if line[2] == "^":
    return float(line[1]) ** float(line[3])


def scan_lines(lines: list):
  for line in lines:
    split_line = line.split()
    if "output" in line:
      print(" ".join(split_line[1:]))
    if "operate" in line:
      print(operate_num(split_line))


scan_lines(lines)
