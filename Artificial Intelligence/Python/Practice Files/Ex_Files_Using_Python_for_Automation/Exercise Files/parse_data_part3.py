import json

file_path = "groceries.json"

with open(file_path, "r") as file:
    data = file.read()

parsed_data = json.loads(data)

print("apples quantity:", parsed_data["apples"])