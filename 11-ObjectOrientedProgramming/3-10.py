class C:
    def __init__(self, lista):
        self.lista = lista

    def m(self, n):
        c = 0
        for i in self.lista:
            if i[0] > 0 and i[1] > 0:
                c += 1
        return c >= n

def main():
    klasa1 = C([[2,3],[1,8],[-6,4],[3,-7]])
    print(klasa1.m(2))

if __name__ == "__main__":
    main()