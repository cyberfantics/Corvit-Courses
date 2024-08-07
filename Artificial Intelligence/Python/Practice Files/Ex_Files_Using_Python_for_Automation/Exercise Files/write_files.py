# open inputFile.txt with the intention of reading it
inputFile = open("inputFile.txt", "r")

# open passFile.txt with the intention of writing it
passFile = open("passFile.txt", "w")

# open failFile.txt with the intention of writing it
failFile = open("failFile.txt", "w")

# loop through each line in inputFile.txt
# uncomment the following lines of code and fill in
for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)

# close inputFile.txt
inputFile.close()

# close passFile.txt
passFile.close()

# close failFile.txt
failFile.close()