class Phone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        print(f"The phone {self.brand} was turned off")
    
    def turn_on(self):
        self.is_on = True
        print(f"The phone {self.brand} is now on")

    def show_parametrs(self):
        print(f"Your {self.brand}'s parametrs:")
        print(f"Your {self.brand} model: {self.model}")
        print(f"Battery is {self.battery}%")

def main():
    phone1 = Phone("Samsung", "Galaxy", 80)
    phone1.turn_off()
    phone1.turn_on()
    phone1.show_parametrs()
if __name__=="__main__":
    main()

phone2 = Phone("Apple", "16 Pro", 20)
phone2.turn_off()
phone2.turn_on()
phone2.show_parametrs()