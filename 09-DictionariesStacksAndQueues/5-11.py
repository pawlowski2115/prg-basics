import json

voting_file = 'voting.json'

with open(voting_file, 'r', encoding="utf-8") as file:
    voting_results = json.load(file)

# Read the contents of the json file
...

# Vote for a person
person_name = input('Name of the person you are voting for:')
...

# Save voting data to json file
...