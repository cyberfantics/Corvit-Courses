# Read the file and print its contents
with open('dressInfo.txt', 'r') as file:
    for line in file:
        data = line.strip().split(', ')
        count = data[0]
        dress = data[1]
        price = data[2]
        
        print(f"Count: {count}")
        print(f"Dress: {dress}")
        print(f"Price: {price}")
        print()
