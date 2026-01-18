import statistics

class Statistica:
    def __init__(self):
        self.numbers = []
    
    def add(self, num):
        self.numbers.append(num)
    
    def show(self):
        for i in self.numbers:
            print(i, end=" ")
        print("")

    def the_greatest(self):
        self.max_num = max(self.numbers)
    
    def the_smallest(self):
        self.min_num = min(self.numbers)
    
    def average(self):
        self.avg = sum(self.numbers)/len(self.numbers)
    
    def mediana(self):
        sorted_numbers = sorted(self.numbers)
        l = len(sorted_numbers)
        mid = l // 2
        if l % 2 == 0:
            self.median = (sorted_numbers[mid]+sorted_numbers[mid-1])/2
        else:
            self.median = sorted_numbers[mid] 

    def med(self):
        self.median2 = statistics.median(self.numbers)


    def results(self):
        print(f"The greatest number: {self.max_num} \nThe smallest number: {self.min_num}")
        print(f"The arithmetic mean of numbers: {self.avg:.2f} \nThe median: {self.median} lub {self.median2}")

    
def main():
    stat = Statistica()
    stat.add(12)
    stat.add(37)
    stat.add(6)
    stat.add(9)
    stat.add(17)
    stat.show()
    stat.the_greatest()
    stat.the_smallest()
    stat.average()
    stat.mediana()
    stat.med()
    stat.results()


if __name__ == "__main__":
    main()