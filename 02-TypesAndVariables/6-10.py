###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print(f'Number of characters: {len(movie)}')

# print title in capital letters
print(f'Title in capital letters: {movie.upper()}')

# print title in small letters
print(f'Title in small letters: {movie.lower()}')

# print how many times the vowel "e" appears in the title
print(f'Number of times "e" appears: {movie.count("e")}')

# print where in the text is the word "Lord"
print(f'Position of the word "Lord": {movie.find("Lord")}')

# print where in the text is the word "dragon"
print(f'Position of the word "dragon": {movie.find("dragon")}')