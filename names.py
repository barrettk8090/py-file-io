names = []

# if opening a file to read, don't need "r" (default behavior)
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {names}")