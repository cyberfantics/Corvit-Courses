inputFile = open("inputFile.txt", "r")
for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)
inputFile.close()