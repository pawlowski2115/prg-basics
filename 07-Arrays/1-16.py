# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
distances_sorted = sorted(distances_traveled)
print(distances_sorted)

# Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
temperatures_sorted = sorted(daily_temperatures, reverse=True) #reverse=True -> sortuje od najwyzszej do najnizszej
print(temperatures_sorted)

# Sort the data in ascending order
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt", "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
file_sorted = sorted(file_names)
print(file_sorted)