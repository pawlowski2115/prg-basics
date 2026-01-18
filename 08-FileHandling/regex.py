import re

test_string = "123abc456abc"

pattern = re.compile(r"abc")
matches = pattern.findall(test_string)

for match in matches:
    print(match)