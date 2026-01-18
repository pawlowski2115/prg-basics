class C:
    def __init__(self,n):
        self.n = n
    
    def m1(self):
        return self.n
    
    def m2(self):
        self.n +=1

    def m3(self):
        self.n -=1

    def m4(self, q):
        self.n = self.n + q

    def __str__(self):
        return f"{self.n}"


