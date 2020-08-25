PATH = "main.ez"

lines = []

with open(PATH, "r") as f:
  for index, value in enumerate(f.readlines()):
    lines.append(value.strip("\n"))
  lines = [i for i in lines if i] 


# Peforms a math operation using [+, -, *, /]
def operate_num(line: list) -> float:
  if line[2] == "+":
    return float(line[1]) + float(line[3])
  if line[2] == "-":
    return float(line[1]) - float(line[3])
  if line[2] == "*":
    return float(line[1]) * float(line[3])
  if line[2] == "/":
    return float(line[1]) / float(line[3])
  if line[2] == "**":
    return float(line[1]) ** float(line[3])


# Checks if an expression is true or false
def check_if(line: list) -> float:
  args = []
  for arg in line[1:]:
    args.append(arg)
  if args[1] == "==":
    if args[0] == args[2]:
      return "True"
    else:
      return "False"
  elif args[1] == "<":
    if args[0] < args[2]:
      return "True"
    else:
      return "False"
  elif args[1] == ">":
    if args[0] > args[2]:
      return "True"
    else:
      return "False"
  elif args[1] == "<=":
    if args[0] <= args[2]:
      return "True"
    else:
      return "False"
  elif args[1] == "!=":
    if args[0] != args[2]:
      return "True"
    else:
      return "False"
  elif args[1] == ">=":
    if args[0] >= args[2]:
      return "True"
    else:
      return "False"


# Scans the line for key words
def scan_lines(lines: list):
  for line in lines:
    split_line = line.split()
    if "output" in line:
      print(" ".join(split_line[1:]))
    if "add" in line:
      print(operate_num(split_line))
    if "if" in line:
      print(check_if(split_line))


scan_lines(lines)
