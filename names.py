with open("names.txt", "r") as file:
    lines = file.readlines()

# basic implementation would print each name on a new line
# can either use , end="" after "line" in the print statement 
# or use line.rstrip()
for line in lines:
    print("hello,", line.rstrip())