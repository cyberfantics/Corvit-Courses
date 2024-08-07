import re

# uncomment the following line of code and fill in 
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

example = "The number is 123-456-7890."

# uncomment the following line of code and fill in 
result = phoneNumRegex.search(example)

# uncomment the following lines of code and fill in 
if result:
    print("Phone number found:", result.group())
    print("Area code:", result.group()[0:3])