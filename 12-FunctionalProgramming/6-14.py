bottles = [508,500,512,499,492,511,503,476,501,509]
test = list(filter(lambda x: x > 500 * 1.02 or x < 500 *0.98, bottles))
incorrectly = len(test)/len(bottles) *100

print("Bottle capacity:    500ml")
print("Filling tolerance:  2%")
print(f"Filled bottles: , {test}")
print("Incorrectly filled: ",incorrectly,"%")


#do poprawy -> funkcja wyszego rzedu (obligatory!)