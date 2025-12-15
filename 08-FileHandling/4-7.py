import re

text = input("Your text: ")

pattern = r'[aeiouAEIOU]'

vowels_found = re.findall(pattern, text)
num_vowels = len(vowels_found)

print(vowels_found)
print(num_vowels)