names = []

# if opening a file to read, don't need "r" (default behavior)
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
