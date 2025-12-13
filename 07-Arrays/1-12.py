categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = expenses[0]
max_categories = categories[0]


for i in range(len(expenses)):
    if expenses[i] > max_expense:
        max_expense = expenses[i]
        max_categories = categories[i]

print(f'The most expensive category is {max_categories}')