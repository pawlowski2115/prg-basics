class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        result = f"{self.surname}{self.name[0]}"
        if self.age >= 18:
            return f"{result.upper()}{self.seniority}"
        else:
            return f"{result.lower()}{self.seniority}"


def main():
    print(C("Anna","May",17,7))
    print(C("George","Brown",21,4))

if __name__ == "__main__":
    main()