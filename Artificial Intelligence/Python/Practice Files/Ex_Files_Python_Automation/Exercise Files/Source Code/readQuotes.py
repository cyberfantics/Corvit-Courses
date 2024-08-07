# Read the file and print its contents
with open('quotes.txt', 'r') as file:
    for line in file:
        data = line.strip().split('-+-')
        quote = data[0]
        author = data[1]
        tags = data[2]
        
        print(f"Quote: {quote}")
        print(f"Author: {author}")
        print(f"Tags: {tags}")
        print()
