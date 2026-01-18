import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = 0.0
    
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
    
    def test(self):
        if self.is_on == True:
            self.temperature = round(random.uniform(34.0,42.0),1)         
    
    def display(self):
        if self.temperature >= 37 and self.temperature < 41:
                print(f"Temperature: {self.temperature}C (fever)")
        elif self.temperature >= 41:
            print(f"Temperature: {self.temperature}C (fever)\nCRITICAL TEMPERATURE!!")
        else:
            print(f"Temperature {self.temperature}")
            


def main():
    temp = Thermometer()
    temp.turn_on()
    temp.test()
    temp.display()
    temp.turn_off()

if __name__ == "__main__":
    main()
