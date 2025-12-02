q1 = input("SURVEY Are you interested in computer science? (y/n): ")
q2 = input("Do you like playing computer games? (y/n): ")
q3 = input("Do you have an Instagram account? (y/n): ")

answear_q1 = (q1 == "y")
answear_q2 = (q2 == "y")
answear_q3 = (q3 == "y")

print("SURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if answear_q1 else 'No'}")
print(f"Likes playing computer games: {'Yes' if answear_q2 else 'No'}")
print(f"Has an Instagram account: {'Yes' if answear_q3 else 'No'}")