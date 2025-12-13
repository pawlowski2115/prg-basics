# Tygodniowe wydatki dla różnych kategorii: [Żywność, Transport, Media]
monthly_expenses = [
   [200, 50, 100],  # Tydzień 1
   [180, 60, 110],  # Tydzień 2
   [220, 55, 105],  # Tydzień 3
   [210, 65, 95]    # Tydzień 4
]

# Kategorie (dla lepszej czytelności)
CATEGORIES = ["Food", "Transport", "Utilities"]
NUM_WEEKS = len(monthly_expenses)     # 4
NUM_CATEGORIES = len(CATEGORIES) # 3

# 1. Inicjalizacja sum
# Sumy dla każdej kategorii (3 sumy)
total_category_expenses = [0] * NUM_CATEGORIES

# Sumy dla każdego tygodnia (4 sumy)
total_week_expenses = [0] * NUM_WEEKS

total_month_expense = 0

# 2. Obliczanie wydatków za pomocą pętli
# Używamy zagnieżdżonych pętli for:
# Pętla zewnętrzna iteruje przez tygodnie (wiersze)
for i in range(NUM_WEEKS):
    week_sum = 0
    # Pętla wewnętrzna iteruje przez kategorie (kolumny) w danym tygodniu
    for j in range(NUM_CATEGORIES):
        expense = monthly_expenses[i][j]

        # A. Dodanie do sumy kategorii (kolumny)
        total_category_expenses[j] += expense

        # B. Dodanie do sumy tygodnia (wiersza)
        week_sum += expense

        # C. Dodanie do sumy miesięcznej (sumowanie wszystkiego)
        total_month_expense += expense

    # Zapisanie sumy tygodnia
    total_week_expenses[i] = week_sum


# 3. Drukowanie wyników
print('MONTHLY EXPENSES')
print('----------------')

# Wypisanie wydatków według kategorii
print(f'{CATEGORIES[0]}: {total_category_expenses[0]}')
print(f'{CATEGORIES[1]}: {total_category_expenses[1]}')
print(f'{CATEGORIES[2]}: {total_category_expenses[2]}')
# Można też użyć pętli, aby to zrobić dynamicznie:
# for k in range(NUM_CATEGORIES):
#     print(f'{CATEGORIES[k]}: {total_category_expenses[k]}')

# Wypisanie wydatków według tygodni
print(f'Week 1: {total_week_expenses[0]}')
print(f'Week 2: {total_week_expenses[1]}')
print(f'Week 3: {total_week_expenses[2]}')
print(f'Week 4: {total_week_expenses[3]}')
# Można też użyć pętli, aby to zrobić dynamicznie:
# for w in range(NUM_WEEKS):
#     print(f'Week {w+1}: {total_week_expenses[w]}')

print('---------------')
print(f'TOTAL: {total_month_expense}')