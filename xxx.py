
cows = []


class Cow:
    def __init__(self, age):
        self.age = age

    def add_age(self):
        self.age += 1
        if self.age >= 4:
            cows.append(Cow(0))


if __name__ == '__main__':
    cows.append(Cow(1))
    n = 11
    for i in range(n-1):
        for cow in cows:
            cow.add_age()
    print(len(cows))
