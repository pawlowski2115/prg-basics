computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games.sort() # Sort the list in alphabetical order
index = 1
i = 0
while i < len(computer_games):
   print(f'{index}. {computer_games[i]}')
   i += 1
   index += 1