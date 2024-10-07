name = input("What's your name? ")

# open a file and write to it, but this recreates and overwrites the file.
# file = open("names.txt", "w")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()