# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]


# Zwraca nazwę dnia tygodnia
def weekday(n):
   """
   Zwraca nazwę dnia tygodnia (np. "Monday") dla podanego numeru (1-7).
   """
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   # Pamiętaj, że lista jest indeksowana od 0, więc dla dnia 1, używamy indeksu n-1.
   return weekdays[n-1]

# Zwraca ciąg znaków z nazwami posiłków dla danego dnia
# oddzielonymi przecinkami
def day_meal_plan(meal_plan, day_number):
   """
   Zwraca posiłki dla danego dnia jako jeden ciąg znaków oddzielony przecinkami.
   'day_number' jest liczbą od 1 do 7.
   """
   # Wybieramy listę posiłków dla danego dnia.
   # Używamy day_number - 1, aby uzyskać prawidłowy indeks (0 do 6).
   day_meals = meal_plan[day_number - 1]
   
   # Używamy metody join() do połączenia elementów listy za pomocą przecinka i spacji.
   return ", ".join(day_meals)

# Główna część programu: Drukowanie tygodniowego planu posiłków
print('WEEKLY MEAL PLAN')
print('(Breakfast, Lunch, Dinner)')
print('==========================')

# Pętla przez wszystkie 7 dni tygodnia (używając numerów 1 do 7)
for day_num in range(1, 8):
   # Pobieramy nazwę dnia (np. "Monday")
   day_name = weekday(day_num)
   
   # Pobieramy posiłki na dany dzień w formacie "Śniadanie, Obiad, Kolacja"
   meals = day_meal_plan(meal_plan, day_num)
   
   # Drukowanie wyniku w formacie "Dzień: Posiłek1, Posiłek2, Posiłek3"
   print(f'{day_name}: {meals}')