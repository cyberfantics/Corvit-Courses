import csv

file_path = "groceries.csv"

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    for row in csv_reader:
        row[1] = int(row[1])
        print(row)