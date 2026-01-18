class C:
    def __init__(self, sectors):
        self.sectors = sectors
        
    def m1(self,s,n):
        self.sectors[s]=n
    
    def m2(self, s):
        sum = 0
        for i in s:
            if i in self.sectors:           #sprawdzamy czy sektor istnieje (czy wartość i jest w słowniku jako klucz)
                sum += self.sectors[i]
        return sum

def main():
    stadion = C({"A":120,"D":150,"G":90,"K":110})
    stadion.m1("G",130)
    print(stadion.m2("GD"))
    print(stadion.m2("KEJ"))

if __name__ == "__main__":
    main()

    