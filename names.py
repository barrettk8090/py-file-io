name = input("What's your name? ")

# using with statements - autocloses the file
with open("names.txt", "a") as file: 
    file.write(f"{name}\n")