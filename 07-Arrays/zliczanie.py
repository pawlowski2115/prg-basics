# Weekly expenses for different categories
categories = ["Food", "Transport", "Utilities"]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

num_weeks = len(monthly_expenses)     # 4
num_categories = len(categories) # 3
total_sum = 0
total_week = [0] * num_weeks
total_category = [0] * num_categories
# Calculates expenses
# Use loop statements

for i in range(num_weeks):
    week_sum = 0
    for j in range(num_categories):
        # Add to category total
        total_category[j] = total_category[j] + monthly_expenses[i][j]
        # Add to week total
        week_sum = week_sum + monthly_expenses[i][j]
        # Add to month total
        total_sum = total_sum + monthly_expenses[i][j]
    total_week[i] = week_sum
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_category[0])
print('Transport:', total_category[1])
print('Utilities:', total_category[2])
print('Week 1:',total_week[0])
print('Week 2:',total_week[1])
print('Week 3:',total_week[2])
print('Week 4:', total_week[3])
print('---------------')
print('TOTAL:', total_sum)